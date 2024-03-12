from datetime import datetime, timedelta
users = [
    {"name": "Lexa Doe", "birthday": "1975.03.20"},
    {"name": "Jane Mois", "birthday": "1990.03.16"},
    {"name": "Alex Smith", "birthday": "2023.03.12"},
    {"name": "Jane Mois", "birthday": "1990.03.19"}
]

def now_year (users): # перевод на сьодняшній рік
    
    today = datetime.today().date()
    birthday_this_year = []
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=today.year)
        if birthday < today and birthday.weekday() < 5: 
            birthday = birthday.replace(year=today.year + 1)
        birthday_this_year.append({"name": user['name'], "birthday": birthday})
    return birthday_this_year

def week(users): # перенос дня, якщо вихідний()
    
    birthday_week = []
    
    for user in users:
        if user["birthday"].weekday() == 5:
            perenos_day5 = timedelta(days=2)
            user["birthday"] = user["birthday"] + perenos_day5
        elif user["birthday"].weekday() == 6:
            perenos_day6 = timedelta(days=1)
            user["birthday"] = user["birthday"] + perenos_day6
        birthday_week.append({"name": user['name'], "birthday": user["birthday"]})
    return birthday_week

def get_upcoming_birthdays(users): # збираємо день народження, якщо на цьому тижні
    
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in week(now_year(users)):
        delta = user["birthday"].toordinal() - today.toordinal()
        if 0 <= delta <= 7:
            birthday_str = user["birthday"].strftime('%Y.%m.%d') 
            upcoming_birthdays.append({"name": user['name'], "congratulation_date": birthday_str})
    return upcoming_birthdays

get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))
