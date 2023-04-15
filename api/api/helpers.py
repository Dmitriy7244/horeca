import re
from datetime import datetime


def safe_html(text: str) -> str:  # TODO
    """Escape "<" and ">" symbols that are not a part of a tag."""
    return re.sub(
        pattern="<(?!(/|b>|i>|u>|s>|tg-spoiler>|a>|a href=|code>|pre>|code class=))",
        repl="&lt;",
        string=text,
    )


def uncapitalize(text: str):
    return text[0].lower() + text[1:]


def repr_timestamp_as_date(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime("%d.%m.%Y %H:%M")
