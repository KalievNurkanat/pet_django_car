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
    

def validate_ballance(buyer, car):
    if car.price > buyer.ballance:
        raise ValueError("Not enough balance")

    seller = car.author

    buyer.ballance -= car.price
    seller.ballance += car.price

    buyer.save()
    seller.save()
    


