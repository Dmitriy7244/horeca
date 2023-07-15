import re

from . import models
from .lib import safe_html, uncapitalize
from .texts import texts


def repr_company_info(info: models.CompanyInfo):
    address = uncapitalize(info.address)
    if info.city != info.region:
        address = f"{info.city}, {address}"

    return texts.COMPANY_INFO_REPR.format(
        type=uncapitalize(info.type),
        name=info.name,
        address=address,
    )


def repr_vacancy(vacancy: models.Vacancy):
    salary = re.sub(r"(\d+)", r"<b>\1</b>", vacancy.salary)
    schedule = re.sub(r"(\d+)", r"<b>\1</b>", vacancy.schedule)
    working_hours = re.sub(r"(\d+)", r"<b>\1</b>", vacancy.working_hours)

    return texts.VACANCY_REPR.format(
        title=vacancy.title,
        work_experience=uncapitalize(vacancy.work_experience),
        salary=uncapitalize(salary),
        schedule=schedule,
        working_hours=uncapitalize(working_hours),
    )


def repr_extra_info(info: models.ExtraInfo, with_photo: bool):
    photo = texts.HIDDEN_URL.format(info.photo) if with_photo else ""
    text = texts.OTHER_INFO_REPR.format(
        additional_info=info.extra_info,
        photo=photo,
        contact_phone=info.phone,
    )
    return text.strip()


def repr_ad(ad: models.Ad, with_photo=True):
    text = texts.AD_REPR.format(
        company_info=repr_company_info(ad.company_info),
        vacancies="\n\n".join([repr_vacancy(v) for v in ad.vacancies]),
        extra_info=repr_extra_info(ad.extra_info, with_photo),
    )
    return safe_html(text.replace("\n" * 3, "\n" * 2))


def repr_invoice(invoice: models.Invoice):
    result = texts.AD_PRICE.format(invoice.vacancies_price)
    if invoice.pinning_price:
        result += texts.PIN_PRICE.format(invoice.pinning_price) + "\n"
    if invoice.duplicating_price:
        result += texts.DUPLICATE_PRICE.format(invoice.duplicating_price) + "\n"
    return result + texts.TOTAL_PRICE.format(invoice.total_price)
