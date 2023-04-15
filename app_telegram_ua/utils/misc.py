import re
from contextlib import suppress
from datetime import datetime
from typing import Optional


def parse_phone_number(msg_text: str) -> Optional[str]:
    digits = ''.join(re.findall(r'\d', msg_text))

    if len(digits) == 10:
        digits = '38' + digits

    if not len(digits) == 12:
        return None

    return f'+{digits[:2]} ({digits[2:5]}) {digits[5:8]} {digits[8:10]} {digits[10:12]}'


def parse_post_date(msg_text: str) -> Optional[float]:
    for fmt in ['%d.%m.%y %H:%M', '%d.%m.%Y %H:%M']:
        with suppress(Exception):
            return datetime.strptime(msg_text, fmt).timestamp()
    raise ValueError('Wrong post date')


def get_word_form(amount: int, form_for_1_unit: str, form_for_2_units: str, form_for_5_units: str):
    tens, units = divmod(amount, 10)
    if tens % 10 == 1:
        return form_for_5_units
    if units == 1:
        return form_for_1_unit
    if units in range(2, 5):
        return form_for_2_units
    return form_for_5_units


def uncapitalize(text: str):
    return text[0].lower() + text[1:]
