from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    if not users: return {}

    birthday_day = None
    currend_date = date.today()
    current_day = currend_date.strftime("%A")
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    days_of_week = days_of_week[days_of_week.index(current_day):] + days_of_week[:days_of_week.index(current_day)]
    
    next_week = currend_date + timedelta(days=7)
    result = {day: [] for day in days_of_week}

    for item in users:
        next_birthday = item["birthday"].replace(year=currend_date.year)

        if currend_date > next_birthday:
            next_birthday = item["birthday"].replace(year=currend_date.year + 1)

        if next_birthday <= next_week:            
            birthday_day = item["birthday"].replace(year=currend_date.year).strftime("%A")

            if birthday_day == "Saturday" or birthday_day == "Sunday":
                birthday_day = "Monday"
            
            result[birthday_day].append(item["name"].split(" ")[0])

    result_copy = result.copy()

    for day, user in result_copy.items():
        if not user:
            result.pop(day)
        
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
