from i_texts import texts as _

from .config import MAX_ANSWER_LEN


class Texts:
    MENU = _[1]
    CREATE_AD = _[2]
    MY_ADS = _[3]
    SUPPORT = _[4]
    OUR_SITE = _[5]
    OTHER_LANG_BOT = _[6]
    CREATE_AD_GUIDE = _[7]
    ASK_REGION = _[8]
    ASK_CITY = _[9]
    ASK_COMPANY_TYPE = _[10]
    ASK_COMPANY_NAME = _[11]
    ASK_ADDRESS = _[12]
    ASK_VACANCY_AMOUNT = _[13]
    VACANCIES_PRICE = _[14]
    VACANCY_NUM = _[15]
    ASK_VACANCY_TITLE = _[16]
    ASK_WORK_EXPERIENCE = _[17]
    ASK_SALARY = _[18]
    NO_DIGITS_ERROR = _[19]
    ASK_SCHEDULE = _[20]
    ASK_WORKING_HOURS = _[21]
    VACANCIES_FILLED = _[22]
    ASK_EXTRA_INFO = _[23]
    SKIP = _[24]
    ANSWER_LEN_ERROR = _[25].format(MAX_ANSWER_LEN)
    PHONE_FORMAT = _[26]
    SEND_PHONE = _[27]
    ASK_PHONE = _[28].format(PHONE_FORMAT)
    PHONE_ERROR = _[29].format(PHONE_FORMAT)
    ASK_PHOTO = _[30]
    PHOTO_FILE_ERROR = _[31]
    NOT_PIN = _[32]
    PIN = _[33]
    ASK_PIN_OPTION = _[34]
    PIN_DELAY = _[35]
    ASK_AD_EDIT = _[36]
    EDIT_COMPANY = _[37]
    EDIT_VACANCY = _[38]
    EDIT_OTHER_INFO = _[39]
    DONE = _[40]
    DATE_FORMAT = _[41]
    ASK_POST_DATE = _[42].format(DATE_FORMAT)
    DATE_FORMAT_ERROR = _[43].format(DATE_FORMAT)
    PAST_DATE_ERROR = _[44]
    ASK_DUPLICATE_OPTION = _[45]
    NOT_DUPLICATE = _[46]
    DUPLICATE = _[47]
    AD_REPR = _[48]
    COMPANY_INFO_REPR = _[49]
    VACANCY_REPR = _[50]
    OTHER_INFO_REPR = _[51]
    PIN_PRICE = _[52]
    DUPLICATE_PRICE = _[53]
    AD_PRICE = _[54]
    TOTAL_PRICE = _[55]
    PAYMENT_FOR_ORDER = _[56]
    BACK = _[57]
    CITY = _[58]
    COMPANY_TYPE = _[59]
    COMPANY_NAME = _[60]
    COMPANY_ADDRESS = _[61]
    VACANCY_TITLE = _[62]
    WORK_EXPERIENCE = _[63]
    SALARY = _[64]
    SCHEDULE = _[65]
    WORKING_HOURS = _[66]
    EXTRA_INFO = _[67]
    PHONE = _[68]
    PHOTO = _[69]
    PIN_OPTION = _[70]
    DUPLICATE_OPTION = _[71]
    POST_DATE = _[72]
    ASK_ITEM_TO_EDIT = _[73]
    PAY = _[74]
    ORDER_NOT_FOUND = _[75]
    ORDER_PUBLISHED = _[76]
    PAYMENT_SUCCESS = _[77]
    NEW_ORDER = _[78]


texts = Texts()
