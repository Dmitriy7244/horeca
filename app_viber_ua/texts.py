choose_regional_city = "Виберіть обласне місто:"
choose_city = "Виберіть одне з міст:"
main_menu = "Головне меню:"

send_phone_number = 'Надіслати свій номер телефону'

company_type = "Тип закладу"
enter_company_type = """
🏨 <b>Вкажіть ваш тип закладу</b> :
(ресторан, бар, кафе, кав'ярня, отель, кальянная, готель, паб і інше)
"""

company_name = 'Назва закладу'
enter_company_name = """
⚜️ <b>Вкажіть назву закладу</b>
(наприклад: Alaska, Jord, Catch, Azuma, Fratelli, Goodman, Coast і так далі)
"""

company_address = 'Адреса закладу'
enter_company_address = """
📍 <b>Вкажіть адресу закладу</b>
(наприклад: вулиця, провулок, площа, бульвар, проспект і так далі)
"""

enter_vac_title = """
👤 <b>Вкажіть назву вакансії</b> :
(кухар, офіціант, бармен, бариста, посудомийниця, прибиральниця і т.д.)
"""

enter_work_experience = """
📈 <b>Необхідний досвід роботи</b>
(наприклад: від 1-го року, від 2-х років, від 5-ти років, не обов'язковий і т.д.)
"""

enter_salary = """
💵 <b>Вкажіть зарплату (у цифрах)</b>
(ставка, відсоток, зміна, на місяць, +бонуси, +преміальні і т.д.)
"""

enter_schedule = """
📆 <b>Вкажіть графік роботи</b>
(наприклад: 3/3, 5/2, добовий ½)
"""

enter_working_hours = """
⏰ <b>Вкажіть час роботи</b>
(наприклад: з 08.30 до 22.00)
"""

enter_additional_info = """
📝 <b>Додаткова інформація</b>
(бажана стать, вік, харчування, оплата таксі, оформлення і т.д.)
"""

phone_format = '+38 xxx xxx xx xx'

enter_contact_phone = f"""
☎️ <b>Вкажіть ваш контактний номер</b> :
(натисніть на кнопку або напишіть номер у форматі: {phone_format})
"""

enter_phone_in_right_format = f'Введіть телефон в правильному форматі: {phone_format}'

post_date_format = 'ДД.ММ.РР ЧЧ:ХХ'
post_date_example = '(наприклад: 09.06.21 12:00)'

enter_post_date = f"""
📆 <b>Вкажіть дату і час розміщення поста</b> \
(використовуйте кнопку "Пропустити", якщо ви хочете розмістити пост прямо зараз)

Час вказуйте в форматі:
》{post_date_format}
》{post_date_example}
"""

enter_date_in_right_format = f"""
<b>Вкажіть час в правильному форматі</b> : {post_date_format}
{post_date_example}
"""

enter_later_date = 'Помилка, вкажіть, будь ласка, час більше поточного'

post_date = 'Час розміщення поста'

vacancies_are_filled = '✅ <b>Вакансії заповнені</b>'

send_photo = """
🎞 <b>Надішліть фотографію</b>
(горизонтальну – 16:9 / 4:3)
"""

send_photo_not_file = 'Будь ласка, надішліть зображення як фото, а не як файл'

whether_pin_ad = "📌 <b>Закріпити оголошення на тиждень в шапці каналу?</b>"

whether_duplicate_ad = '📑 <b>Дублювати чи щодня оголошення протягом тижня?</b>'

must_be_integer = "Цей параметр обов'язково має бути вказаний цифрами і буквами"

create_ad_btn = "📝 Створити оголошення"
create_ad_guide = """
》Щоб створити оголошення, вам необхідно пройти поетапно декілька наступних кроків:

1) Вказати основну інформацію про заклад
2) Додати від 1 до 3-х вакансій
3) Вказати додаткову інформацію/послуги/контакти

У самому кінці можна подивитися, як виглядатиме ваше оголошення і при необхідності змінити будь-яку інформацію 
"""

my_ads_btn = "📁 Мої оголошення"
tech_support_btn = "👨‍💻 Техпідтримка"
our_site_btn = "🌐 Наш сайт"
choose_vacs_num = 'Виберіть, скільки вакансій Ви плануєте розміщувати?'
payment_succeeded = 'Платіж успішно проведений! Чекайте модерацію поста адміністраторами групи'

pinning_able_time = "📆 Послуга «Закріплення» стане доступна з {}"

back_btn = "🔙 Назад"
pay_up = 'Оплатити'

vac_word_forms = 'вакансія;вакансії;вакансій'
day_word_forms = 'день;дня;днів'

not_pin = 'Не закріплювати'
pin_for = 'Закріпити - {price} грн.'
duplicate = 'Дублювати - {price} грн.'
not_duplicate = 'Не дублювати'

vac_num = '<b>Вакансія №{}</b>'
another_lang_bot = '🇷🇺 Бот на рус. языке'

do_you_wanna_change_ad = 'Чи бажаєте ви змінити яку-небудь інформацію в цьому оголошенні?'

ad_template = """
{company_info}

{vacancies}

{extra_info}
"""

company_info_template = """\
<b>В {type} «{name}»</b>
{address}
Потрібен:\
"""

vacancy_template = """\
 • <b>{title}</b>
Досвід роботи {work_experience}
З/п 💵 {salary}
📆 Графік роботи {schedule}
⏰ {working_hours}\
"""

extra_info_template = """\
{additional_info}

Звертатися за тел.:
📲 {contact_phone}\
"""

company_info = 'Інформація про компанію'
vacancy_num = 'Вакансію №{vac_num}'
extra_info = 'Іншу інформацію'
all_good = 'Ні, все добре'

vacancies_num_and_prices = '{num} {vac_word} - {price} грн.'

which_item_you_wanna_change = 'Який пункт ви бажаєте змінити?'

regional_city = 'Обласне місто'
city = 'Конкретне місто'
type = 'Тип закладу'
name = 'Назва закладу'
address = 'Адреса закладу'

vacancy_title = 'Назва вакансії'
work_experience = 'Необхідний досвід роботи'
salary = 'Заробітна плата'
schedule = 'Графік роботи'
working_hours = 'Час роботи'

additional_info = 'Додаткова інформація'
contact_phone = 'Контактний номер телефону'
photo = 'Фотографія закладу'

pinning = 'Послуга: «Закріплення»'
duplicating = 'Послуга: «Дублювання»'

pinning_price = '📌 Закріплення: +{pinning_price}₴'
duplicating_price = '📑 Дублювання: +{duplicating_price}₴'

vacancies_price = """
Замовлення прийняте! Посилання для оплати:
------------------------------------------------
📝 Ціна оголошення: {vacancies_price}₴
"""

total_price = """\
------------------------------------------------
💵 <b>Разом до сплати– {total_price}₴</b>
"""

vacancy_not_exists = 'Помилка, немає такої вакансії'
miss = 'Пропустити'

photo_to_narrow = 'Ця фотографія занадто вузька'

pay = 'Оплатити'
delete = 'Видалити'
check_payment = 'Перевірити оплату'

succeeded_payment = """
<b>Платіж успішно проведений!</b>
Чекайте модерацію поста адміністраторами групи
"""

answer_on_message_to_moderate = 'Дайте відповідь на це повідомлення відредагованою версією'

cities = """
Одеса: Одеса, Чорноморськ, Грибівка, Затока, Ізмаїл, Кароліно-Бугаз, Коблеве, Южне, Білгород-Дністровський
Київ: Київ, Біла Церква, Бориспіль, Боярка, Бровари, Буча, Вишневе, Вишгород, Ірпінь, Українка, Фастів
Харків: Харків, Лозова, Куп'янськ, Ізюм
Дніпр: Дніпр, Кривий Ріг, Кам'янське, Нікополь, Павлоград, Новомосковськ
Львів: Львів, Борислав, Дрогобич, Самбір, Стрий, Червоноград
"""

order_approved = '✅ Ваш пост пройшов модерацію, був схвалений і розміщений на всіх наших ресурсах «HoReCa Job»'

pinning_will_be_delayed_until = """
⏱ <b>Резерв</b> : Місце закріплення тимчасово зайнято, ваш пост буде закріплений після {date}
"""

dump = '📦 Дамп'
broadcast = '✉️ Рассылка'

description = """\
⚡️ Ми найбільша Українська
Viber-спільнота з пошуку
співробітників в сфері 
громадського Харчування .

Це найпотужніший інструмент 
у Ваших руках, вся потенційно
цільова аудиторія в сегменті 
HoReCa, сфера гостинності .
_________________________________
📂 Ваші оголошення в групі
автоматично дублюються
на всіх наших ресурсах - Viber,
Telegram, Instagram, Facebook

Відео-інструкція до чат-боту:  
🗨  youtu.be/mQmICHydsnk\
"""

menu = 'Меню'

too_long_answer = 'Занадто довга відповідь, максимальна довжина: {max_len}'