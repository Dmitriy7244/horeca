import env

VIBER_MODE = env.get_bool('VIBER_MODE', False)

if VIBER_MODE:
    from viber import (
        run,
        bot,
        app,
        CallbackButton,
        UrlButton,
        InlineKeyboard,
        ReplyKeyboard,
        ContactRequestButton,
        State,
        StatesGroup,
        Dispatcher,
        Message,
        reply,
        CancelHandler,
        dp,
        FSMContext,
        ask,
        get_photo_url,
        CallbackQuery as Query,
    )
else:
    from botty import (
        run,
        bot,
        app,
        CallbackButton,
        UrlButton,
        InlineKeyboard,
        ReplyKeyboard,
        ContactRequestButton,
        State,
        StatesGroup,
        Dispatcher,
        Message,
        reply,
        CancelHandler,
        dp,
        FSMContext,
        ask,
        get_photo_url,
        Query,
    )

Event = Message | Query

__all__ = [
    "run",
    "bot",
    "app",
    "CallbackButton",
    "UrlButton",
    "InlineKeyboard",
    "ReplyKeyboard",
    "ContactRequestButton",
    "State",
    "StatesGroup",
    "Dispatcher",
    "Message",
    "reply",
    "CancelHandler",
    "dp",
    "FSMContext",
    "ask",
    "VIBER_MODE",
    "get_photo_url",
    "Query",
    "Event",
]
