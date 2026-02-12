import datetime


def validate_age(user):
    user_data = user.birth_date
    if not user_data:
        raise ValueError("Enter ur birth date")

    today = datetime.date.today()

    birthday = user_data

    age = today.year - birthday.year

    if age < 18:
        raise ValueError("U must be 18 years old")