from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from mongoengine import Document, EmbeddedDocument, IntField, ListField
from mongoengine import StringField, EmbeddedDocumentField, EmbeddedDocumentListField, BooleanField


class CompanyInfo(EmbeddedDocument):
    regional_city = StringField()
    city = StringField()
    type = StringField()
    name = StringField()
    address = StringField()


class Vacancy(EmbeddedDocument):
    title = StringField()
    work_experience = StringField()
    salary = StringField()
    schedule = StringField()
    working_hours = StringField()


class ExtraInfo(EmbeddedDocument):
    additional_info = StringField()
    contact_phone = StringField()
    photo = StringField()
    pin = BooleanField()
    duplicate = BooleanField()
    post_date = IntField()


class Ad(EmbeddedDocument):
    company_info: CompanyInfo = EmbeddedDocumentField(CompanyInfo, default=CompanyInfo)
    vacancies: list[Vacancy] = EmbeddedDocumentListField(Vacancy)
    extra_info: ExtraInfo = EmbeddedDocumentField(ExtraInfo, default=ExtraInfo)


@dataclass
class Invoice:
    vacancies_price: int
    pinning_price: int
    duplicating_price: int

    @property
    def total_price(self):
        return sum([self.vacancies_price, self.pinning_price, self.duplicating_price])


class Order(Document):
    user_id: str = StringField()
    date: int = IntField()
    ad: Ad = EmbeddedDocumentField(Ad)
    price: int = IntField()
    created_from: str = StringField()
    channel_id: int = IntField()

    paid_up: bool = BooleanField(default=False)
    approved: bool = BooleanField(default=False)
    pinned: bool = BooleanField()
    final_ad_text: Optional[str] = StringField()
    post_id: Optional[int] = IntField()
    pin_from: Optional[int] = IntField()
    pin_until: Optional[int] = IntField()
    posts_dates: list[int] = ListField(IntField())
