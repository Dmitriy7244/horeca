import env
import yaml
from pydantic import BaseModel

MAX_ANSWER_LEN = 150
OUR_SITE_URL = "https://horeca-job.com.ua/"
SUPPORT_URL = "https://t.me/LFeedbackBot"
AD_PHOTO_RATIO = 4 / 3
ADMINS_IDS = env.get_ints("ADMINS_IDS")
ADMIN_GROUP = env.get_int("ADMIN_GROUP")
BOT_URI = env.get("BOT_URI")
OTHER_LANG_BOT_URL = env.get("OTHER_LANG_BOT_URL")


class PRICES:
    VACANCIES = {1: 200, 2: 300, 3: 400}
    PIN_OPTION = 1000
    DUPLICATE_OPTION = {1: 800, 2: 1200, 3: 1600}


class MERCHANT:
    _ = "MERCHANT_"
    ID = env.get_int(_ + "ID")
    SECRET_KEY = env.get(_ + "SECRET_KEY")
    CALLBACK_URL = env.get(_ + "CALLBACK_URL")


class MONGO:
    _ = "MONGO_"
    DB = env.get(_ + "DB")
    HOST = env.get(_ + "HOST")
    USER = env.get(_ + "USER", "root")
    PASSWORD = env.get(_ + "PASSWORD")


class Region(BaseModel):
    channel: int
    cities: list[str]


class Config(BaseModel):
    regions: dict[str, Region]

    def get_cities(self, region: str) -> list[str]:
        return [region, *self.regions[region].cities]

    def get_channel(self, region: str) -> int:
        return self.regions[region].channel


with open("../config.yml", encoding="utf8") as stream:
    config = Config(**yaml.safe_load(stream))
