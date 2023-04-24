import re
from datetime import datetime

from .config import MAX_ANSWER_LEN
from .texts import texts


class ApiError(Exception):
    def __init__(self, text: str):
        self.text = text


def parse_post_date(text: str) -> int:
    for fmt in ["%d.%m.%y %H:%M", "%d.%m.%Y %H:%M"]:
        try:
            post_date = datetime.strptime(text, fmt).timestamp()
        except ValueError:
            continue
        if post_date < datetime.now().timestamp():
            raise ApiError(texts.PAST_DATE_ERROR)
        return int(post_date)
    raise ApiError(texts.DATE_FORMAT_ERROR)


def parse_phone(text: str) -> str:
    ds = "".join(re.findall(r"\d", text))
    if len(ds) == 10:
        ds = "38" + ds
    if not len(ds) == 12:
        raise ApiError(texts.PHONE_ERROR)
    return f"+{ds[:2]} ({ds[2:5]}) {ds[5:8]} {ds[8:10]} {ds[10:12]}"


def check_answer_len(text: str):
    if len(text) > MAX_ANSWER_LEN:
        raise ApiError(texts.ANSWER_LEN_ERROR)


def crop_photo(url: str) -> str:  # TODO
    return url and "https://telegra.ph/file/334f0f0dc80e933f61a8c.jpg"


def check_for_digits(text: str):
    if not re.search(r"\d", text):
        raise ApiError(texts.NO_DIGITS_ERROR)
