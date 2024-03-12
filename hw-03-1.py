from datetime import datetime

def get_days_from_today(date):
    now = datetime.today()
    date_now = now.date()
    while True:
        try:
            datetime_object = datetime.strptime(date, "%Y-%m-%d")
            delta = date_now.toordinal() - datetime_object.toordinal()
            return delta
        except ValueError:
            return print(f'{date} Please enter the date in the format "РРРР-ММ-ДД"')

            

print(get_days_from_today("2024-03-05"))


# В умові написано використовувати "datetime.today()"
# І модуль datetime Python
# В конспекті datetime.today() нема. - є тільки datetime.now()
# datetime.today() - з модуля datetime Python не викликається(
# Тому так криво виходило
