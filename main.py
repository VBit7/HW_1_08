"""
Домашнє завдання. Python Core. Модуль 8
"""

from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    """
    Виводить список колег,
    яких потрібно привітати з днем народження на наступному тижні.

    Параметри:
    users (list): Список користувачів, кожен представлений словником
    із ключами 'name' і 'birthday',
    де 'name' - ім'я користувача, 'birthday' - день народження (datetime.date).

    Повертає:
    dict: Словник з днями тижня
    ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    та списками користувачів, яких потрібно привітати на цих днях.
    Враховується наступний тиждень, включаючи поточний день.
    Дні народження, які припадають на вихідні, переносяться на понеділок.

    Приклад використання:
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
    ]
    result = get_birthdays_per_week(users)

    Результат буде у форматі {'Monday': ['Bill', 'Jan'], 'Wednesday': ['Kim']}
    """

    if not users:
        return {}

    currend_date = date.today()
    current_day = currend_date.strftime("%A")
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Переформатовуємо список днів тижня, починаючи з поточного дня
    days_of_week = days_of_week[days_of_week.index(current_day):] + \
        days_of_week[:days_of_week.index(current_day)]

    next_week = currend_date + timedelta(days=7)
    result = {day: [] for day in days_of_week}

    for item in users:

        # Оновлюємо день народження на поточний рік
        next_birthday = item["birthday"].replace(year=currend_date.year)

        # Якщо день народження вже минув у поточному році, то встановлюємо його на наступний рік
        if currend_date > next_birthday:
            next_birthday = item["birthday"].replace(year=currend_date.year + 1)

        # Перевіряємо, чи наступний день народження користувача знаходиться в межах наступного тижня
        if next_birthday <= next_week:
            birthday_day = next_birthday.strftime("%A")

            # Якщо день народження припадає на суботу або неділю, відкладаємо його на понеділок
            if birthday_day in ("Saturday", "Sunday"):
                birthday_day = "Monday"

            result[birthday_day].append(item["name"].split(" ")[0])

    result_copy = result.copy()

    # Якщо список порожній, видаляємо цей день зі словника результатів
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
