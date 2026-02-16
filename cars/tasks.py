from celery import shared_task
from car_sets.settings import EMAIL_HOST_USER, EMAIL_SEND_TO
from django.core.mail import send_mail

@shared_task
def send_via_email(buyer, car):
    send_mail(
        f"Your car was bought by {buyer.username}",
        f"{car.price}$ transferred to your balance",
        EMAIL_HOST_USER, 
        [EMAIL_SEND_TO],
        fail_silently=False
    )
    return "ok"
