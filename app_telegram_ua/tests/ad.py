from models.ad import CompanyInfo, Vacancy, ExtraInfo, Ad

ci = CompanyInfo(
    regional_city='Одесса',
    city='Измаил',
    type='кафе',
    name='IZZI cafe',
    address='пр-т Александровский, 4',
)

v1 = Vacancy(
    title='Повар 👨‍🍳',
    work_experience='от 1-го года',
    salary='700 ставка + бонусы',
    schedule='2/2, 4/2',
    working_hours='с 10:00 до 22:00',
)

v2 = Vacancy(
    title='Помощник повара заготовщик👨‍🍳',
    work_experience='от 1-го года',
    salary='600 ставка + бонусы',
    schedule='2/2',
    working_hours='с 08:00 до 21:00',
)

ei = ExtraInfo(
    additional_info='Предпочтительно до 40 лет, официальное трудоустройство, 🥼 форма, питание 🍲',
    contact_phone='+38 (066) 718 35 27',
    photo='https://i.ibb.co/wpnSfbt/image.png',
    pin=True,
    duplicate=True,
)

ad = Ad(
    company_info=ci,
    vacancies=[v1, v2],
    extra_info=ei,
)

ad = Ad.from_json(ad.to_json())
print(ad)
