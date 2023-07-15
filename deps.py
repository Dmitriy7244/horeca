import env

VIBER_MODE = env.get("PLATFORM") == "viber"

if VIBER_MODE:
    from viber import (
        CallbackButton,
        CancelHandler,
        ContactRequestButton,
        Dispatcher,
        FSMContext,
        InlineKeyboard,
        Message,
        ReplyKeyboard,
        State,
        StatesGroup,
        UrlButton,
        app,
        ask,
        bot,
        dp,
        get_photo_url,
        reply,
        run,
    )
    from viber import (
        CallbackQuery as Query,
    )
else:
    from botty import (
        CallbackButton,
        CancelHandler,
        ContactRequestButton,
        Dispatcher,
        FSMContext,
        InlineKeyboard,
        Message,
        Query,
        ReplyKeyboard,
        State,
        StatesGroup,
        UrlButton,
        app,
        ask,
        bot,
        dp,
        get_photo_url,
        reply,
        run,
    )

    bot.disable_web_page_preview = False

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
