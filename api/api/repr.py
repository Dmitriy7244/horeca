import re

from . import models
from .texts import texts
from .helpers import safe_html


def repr_company_info(info: models.CompanyInfo):
    if info.city != info.region:
        address = f"{info.city}, {info.address}"
    else:
        address = info.address

    return texts.COMPANY_INFO_REPR.format(
        type=info.type,
        name=info.name,
        address=address,
    )


def repr_vacancy(vacancy: models.Vacancy):
    salary = re.sub(r"(\d+)", r"<b>\1</b>", vacancy.salary)
    schedule = re.sub(r"(\d+)", r"<b>\1</b>", vacancy.schedule)
    working_hours = re.sub(r"(\d+)", r"<b>\1</b>", vacancy.working_hours)

    return texts.VACANCY_REPR.format(
        title=vacancy.title,
        work_experience=vacancy.work_experience,
        salary=salary,
        schedule=schedule,
        working_hours=working_hours,
    )


def repr_extra_info(info: models.ExtraInfo):
    text = texts.OTHER_INFO_REPR.format(
        additional_info=info.extra_info,
        photo=info.photo,
        contact_phone=info.phone,
    )
    return text.strip()


def repr_ad(ad: models.Ad):
    text = texts.AD_REPR.format(
        company_info=repr_company_info(ad.company_info),
        vacancies="\n\n".join([repr_vacancy(v) for v in ad.vacancies]),
        extra_info=repr_extra_info(ad.extra_info),
    )
    return safe_html(text)


def repr_invoice(invoice: models.Invoice):
    result = texts.AD_PRICE.format(invoice.vacancies_price)
    if invoice.pinning_price:
        result += texts.PIN_PRICE.format(invoice.pinning_price) + "\n"
    if invoice.duplicating_price:
        result += texts.DUPLICATE_PRICE.format(invoice.duplicating_price) + "\n"
    return result + texts.TOTAL_PRICE.format(invoice.total_price)
