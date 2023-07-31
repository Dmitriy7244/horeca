from dataclasses import dataclass

from mongo import Document, PrimaryKey, me


class CompanyInfo(me.EmbeddedDocument):
    region: str = me.StringField(db_field="regional_city")  # TODO
    city: str = me.StringField()
    type: str = me.StringField()  # noqa: A003
    name: str = me.StringField()
    address: str = me.StringField()


class Vacancy(me.EmbeddedDocument):
    title: str = me.StringField()
    work_experience: str = me.StringField()
    salary: str = me.StringField()
    schedule: str = me.StringField()
    working_hours: str = me.StringField()


class ExtraInfo(me.EmbeddedDocument):
    extra_info: str = me.StringField(db_field="additional_info")  # TODO
    phone: str = me.StringField(db_field="contact_phone")
    photo: str = me.StringField()
    pin: bool = me.BooleanField()
    duplicate: bool = me.BooleanField()
    post_date: int = me.IntField()


class Ad(me.EmbeddedDocument):
    company_info: CompanyInfo = me.EmbeddedDocumentField(
        CompanyInfo, default=CompanyInfo
    )
    vacancies: list[Vacancy] = me.EmbeddedDocumentListField(Vacancy)
    extra_info: ExtraInfo = me.EmbeddedDocumentField(ExtraInfo, default=ExtraInfo)


@dataclass
class Invoice:
    vacancies_price: int
    pinning_price: int
    duplicating_price: int

    @property
    def total_price(self):
        return sum([self.vacancies_price, self.pinning_price, self.duplicating_price])


class Post(Document):
    chat_id: int
    text: str
    pin_from: int | None
    pin_until: int | None
    publish_dates: list[int]
    message_id: int | None


class Order(Document):
    user_id: str
    ad: Ad = me.EmbeddedDocumentField(Ad)
    date: int
    price: int
    channel_id: int
    app_id: str

    notified: bool | None
    paid: bool = me.BooleanField(default=False)
    approved: bool = me.BooleanField(default=False)
    pinned: bool = me.BooleanField()
    final_ad_text: str | None
    post_id: int | None
    pin_from: int | None
    pin_until: int | None
    posts_dates: list[int]


class Webhook(Document):
    app_id: str | PrimaryKey
    url: str
