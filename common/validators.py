from datetime import date
from cars.models import Car

def validate_age(user):
    user_data = user.birth_date
    if not user_data:
        raise ValueError("Enter ur birth date")

    today = date.today()

    birthday = user_data

    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    if age < 18:
        raise ValueError("U must be 18 years old")
    

def validate_ballance(user, car):
    if car.price > user.ballance:
        raise ValueError("Not enough balance")
    user.ballance -= car.price
    user.save()
