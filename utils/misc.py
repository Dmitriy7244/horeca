from __future__ import annotations

import re
from datetime import datetime


def parse_cities(cities_text: str) -> dict[str, list[str]]:
    """Return dict[regional_city:list[city]]"""
    result = {}
    for city_string in cities_text.split('\n'):
        if city_string:
            regional_city, cities = [i.strip() for i in city_string.split(':')]
            result[regional_city] = [c.strip() for c in cities.split(',')]
    return result


def repr_timestamp_as_date(timestamp: int):
    return datetime.fromtimestamp(timestamp).strftime('%d.%m.%Y %H:%M')


def safe_html(text: str) -> str:
    """Escape "<" and ">" symbols that are not a part of a tag."""
    return re.sub(
        pattern='<(?!(/|b>|i>|u>|s>|tg-spoiler>|a>|a href=|code>|pre>|code class=))',
        repl='&lt;',
        string=text,
    )
