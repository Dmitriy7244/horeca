import json

from aiogram_tools.context import storage

from models.ad import Ad, CompanyInfo, Vacancy, ExtraInfo
from models.storage import CreateAdKeys


class _AdProxy:

    @property
    async def ad(self):
        if self._ad is None:
            storage_data = await storage.get_data()
            self._ad = Ad(**storage_data.get('ad', {}))
        return self._ad

    @staticmethod
    async def set_ad(ad: Ad):
        json_dict = json.loads(ad.to_json())
        await storage.update_data({'ad': json_dict})

    def __init__(self):
        self._ad = None

    async def __aenter__(self) -> Ad:
        return await self.ad

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            await self.set_ad(await self.ad)


class CompanyInfoProxy(_AdProxy):

    async def __aenter__(self) -> CompanyInfo:
        ad = await self.ad
        return ad.company_info


class VacancyProxy(_AdProxy):

    async def __aenter__(self) -> Vacancy:
        storage_data = await storage.get_data()
        current_vacancy_num = storage_data[CreateAdKeys.CURRENT_VACANCY_NUM]
        ad = await self.ad

        if len(ad.vacancies) < current_vacancy_num:
            ad.vacancies.append(Vacancy())

        return ad.vacancies[current_vacancy_num - 1]


class ExtraInfoProxy(_AdProxy):

    async def __aenter__(self) -> ExtraInfo:
        ad = await self.ad
        return ad.extra_info


class AdProxy(_AdProxy):

    @staticmethod
    def company_info():
        return CompanyInfoProxy()

    @staticmethod
    def vacancy():
        return VacancyProxy()

    @staticmethod
    def extra_info():
        return ExtraInfoProxy()
