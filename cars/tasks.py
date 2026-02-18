from celery import shared_task
from car_sets.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@shared_task
def send_via_email(buyer, car):
    send_mail(
        f"Your car was bought by {buyer.username}",
        f"{car.price}$ transferred to your balance",
        EMAIL_HOST_USER, 
        [car.author.email],
        fail_silently=False
    )
    return "ok"
