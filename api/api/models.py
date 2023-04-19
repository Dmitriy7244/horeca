from dataclasses import dataclass

from mongoengine import (
    BooleanField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    EmbeddedDocumentListField,
    IntField,
    ListField,
    StringField,
)

from .core import Document


class CompanyInfo(EmbeddedDocument):
    region = StringField(db_field="regional_city")  # TODO
    city = StringField()
    type = StringField()  # noqa: A003
    name = StringField()
    address = StringField()


class Vacancy(EmbeddedDocument):
    title = StringField()
    work_experience = StringField()
    salary = StringField()
    schedule = StringField()
    working_hours = StringField()


class ExtraInfo(EmbeddedDocument):
    extra_info = StringField(db_field="additional_info")  # TODO
    phone: str = StringField(db_field="contact_phone")
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
    channel_id: int = IntField()
    utm: str = StringField()  # TODO
    notified: bool = BooleanField()

    paid: bool = BooleanField(default=False, db_field="paid_up")
    approved: bool = BooleanField(default=False)
    pinned: bool = BooleanField()
    final_ad_text: str | None = StringField()
    post_id: int | None = IntField()
    pin_from: int | None = IntField()
    pin_until: int | None = IntField()
    posts_dates: list[int] = ListField(IntField())


class CreateAdKeys:
    VACANCY_AMOUNT = "vacancy_amount"
    CURRENT_VACANCY_NUM = "current_vacancy_num"
    EDIT_MODE = "edit_mode"
    CURRENT_ORDER_ID = "current_order_id"
