from __future__ import annotations

from typing import Union, Optional

from aiogram.dispatcher.middlewares import MiddlewareManager
from aiogram.utils.mixins import DataMixin, ContextInstanceMixin

from aioviber2 import types
from aioviber2.dispatcher.filters.builtin import (
    Text,
    Regexp,
    IDFilter,
    Command,
    StateFilter,
    ContentTypeFilter,
    ExceptionsFilter,
    MessageButton,
)
from aioviber2.dispatcher.filters.factory import FiltersFactory, Handler
from aioviber2.dispatcher.storage import DisabledStorage, BaseStorage, FSMContext
from aioviber2.types import Update
from aioviber2.bot import Bot


class _Dispatcher(DataMixin, ContextInstanceMixin):

    def __init__(self, bot: Bot, storage: Optional[BaseStorage] = None, loop=None):
        if storage is None:
            storage = DisabledStorage()

        self.bot = bot
        self.storage = storage
        self._main_loop = loop

        self.updates_handler = Handler(self, middleware_key='update')
        self.message_handlers = Handler(self, middleware_key='message')
        self.conversation_started_handlers = Handler(self, middleware_key='conversation_started')
        self.callback_query_handlers = Handler(self, middleware_key='callback_query')
        self.errors_handlers = Handler(self, once=False, middleware_key='error')

        self.updates_handler.register(self.process_update)

        self.filters_factory = FiltersFactory(self)
        self.middleware = MiddlewareManager(self)

        self._setup_filters()

    @property
    def loop(self):
        return self._main_loop

    def _setup_filters(self):
        filters_factory = self.filters_factory

        filters_factory.bind(StateFilter, exclude_event_handlers=[
            self.errors_handlers,
        ])

        filters_factory.bind(ContentTypeFilter, event_handlers=[
            self.message_handlers,
        ]),

        filters_factory.bind(Command, event_handlers=[
            self.message_handlers,
        ])

        filters_factory.bind(Text, event_handlers=[
            self.message_handlers,
            self.callback_query_handlers,
        ])

        filters_factory.bind(Regexp, event_handlers=[
            self.message_handlers,
            self.callback_query_handlers,
        ])

        filters_factory.bind(ExceptionsFilter, event_handlers=[
            self.errors_handlers,
        ])

        filters_factory.bind(IDFilter, event_handlers=[
            self.message_handlers,
            self.callback_query_handlers,
        ])

        filters_factory.bind(MessageButton, event_handlers=[
            self.message_handlers,
        ])

    def current_state(self, *, user: Union[str, int, None] = None) -> FSMContext:
        if user is None:
            user_obj = types.User.get_current()
            user = user_obj.id if user_obj else None

        return FSMContext(storage=self.storage, user=user)


# from aiogram import Dispatcher


class Dispatcher(_Dispatcher):

    def register_message_handler(self, callback, *custom_filters, commands=None, regexp=None, content_types=None,
                                 state=None, **kwargs):
        filters_set = self.filters_factory.resolve(self.message_handlers,
                                                   *custom_filters,
                                                   commands=commands,
                                                   regexp=regexp,
                                                   content_types=content_types,
                                                   state=state,
                                                   **kwargs)
        self.message_handlers.register(callback, filters_set)

    def message_handler(self, *custom_filters, commands=None, regexp=None, content_types=None, state=None,
                        **kwargs):
        def decorator(callback):
            self.register_message_handler(callback, *custom_filters,
                                          commands=commands, regexp=regexp, content_types=content_types,
                                          state=state, **kwargs)
            return callback

        return decorator

    def register_conversation_started_handler(self, callback, *custom_filters, **kwargs):
        filters_set = self.filters_factory.resolve(self.conversation_started_handlers,
                                                   *custom_filters,
                                                   **kwargs)
        self.conversation_started_handlers.register(callback, filters_set)

    def conversation_started_handler(self, *custom_filters, **kwargs):
        def decorator(callback):
            self.register_conversation_started_handler(callback, *custom_filters, **kwargs)
            return callback

        return decorator

    async def process_update(self, update: Update):
        print(update)
        types.Update.set_current(update)

        try:
            if update.message:
                types.Message.set_current(update.message)
                types.User.set_current(update.message.from_user)
                return await self.message_handlers.notify(update.message)
            if update.conversation_started:
                types.ConversationStarted.set_current(update.conversation_started)
                types.User.set_current(update.conversation_started.from_user)
                return await self.conversation_started_handlers.notify(update.conversation_started)
        except Exception as e:
            err = await self.errors_handlers.notify(update, e)
            if err:
                return err
            raise
