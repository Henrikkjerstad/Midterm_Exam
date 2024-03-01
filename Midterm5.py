def days_since_birthday(birthday):
    # Split the birthday string into day, month, and year
    day, month, year = map(int, birthday.split('-'))

    # Calculate the number of complete years since the birthday
    current_year = 2024
    years_since_birthday = current_year - year - 1

    # Calculate the days assuming an average year length of 365.25 days
    days = years_since_birthday * 365.25

    return int(days)


birthday = "07-05-2002"
print(days_since_birthday(birthday))
