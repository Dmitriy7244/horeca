import re

import models.ad as models
import texts


def repr_company_info(info: models.CompanyInfo):
    if info.city != info.regional_city:
        address = f'{info.city}, {info.address}'
    else:
        address = info.address

    return texts.company_info_template.format(
        type=info.type,
        name=info.name,
        address=address,
    )


def repr_vacancy(vacancy: models.Vacancy):
    salary = re.sub(r'(\d+)', r'<b>\1</b>', vacancy.salary)
    schedule = re.sub(r'(\d+)', r'<b>\1</b>', vacancy.schedule)
    working_hours = re.sub(r'(\d+)', r'<b>\1</b>', vacancy.working_hours)

    return texts.vacancy_template.format(
        title=vacancy.title,
        work_experience=vacancy.work_experience,
        salary=salary,
        schedule=schedule,
        working_hours=working_hours,
    )


def repr_extra_info(info: models.ExtraInfo):
    return texts.extra_info_template.format(
        additional_info=info.additional_info,
        contact_phone=info.contact_phone,
    ).strip()


def repr_ad(ad: models.Ad):
    return texts.ad_template.format(
        company_info=repr_company_info(ad.company_info),
        vacancies='\n\n'.join([repr_vacancy(v) for v in ad.vacancies]),
        extra_info=repr_extra_info(ad.extra_info),
    )


def repr_invoice(invoice: models.Invoice):
    result = texts.vacancies_price.format(vacancies_price=invoice.vacancies_price)

    if invoice.pinning_price:
        result += texts.pinning_price.format(pinning_price=invoice.pinning_price) + '\n'

    if invoice.duplicating_price:
        result += texts.duplicating_price.format(duplicating_price=invoice.duplicating_price) + '\n'

    return result + texts.total_price.format(total_price=invoice.total_price)
