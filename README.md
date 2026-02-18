🚗 Car Marketplace (Django)

A simple car marketplace built with Django where users can create, sell, buy, and manage cars with balance transactions and email notifications.

📌 Project Description

This project simulates a small car marketplace:

Users can register and log in.

A user can create a car.

The creator becomes the owner of the car.

The owner can put the car on sale.

The owner can also click "Return from sale", which cancels the selling process.

Other users can buy the car if they have enough balance.

When a car is purchased:

✅ Buyer's balance decreases.

✅ Seller's balance increases.

✅ Seller receives an email notification (handled by Celery).

⚙️ Tech Stack

Backend: Django

Database: PostgreSQL

Task Queue: Celery

Broker / Cache: Redis

Email Notifications: Django Email + Celery

🧠 Business Logic
🔹 Car Creation

A logged-in user creates a car.

The user becomes the author (owner).

The car is not sold by default.

🔹 Put Car On Sale

Owner sets the car as is_sold = False and is_for_sale = True.

🔹 Return From Sale

Owner clicks "Return from sale".

is_for_sale becomes False.

The car is no longer available for purchase.

🔹 Buying a Car

When a user buys a car:

System checks if buyer has enough balance.

Buyer's balance decreases by car.price.

Seller's balance increases by car.price.

Car ownership transfers to buyer.

Car is removed from sale.

Celery sends email notification to the seller.

💸 Balance Logic

If car.price > user.balance → purchase is rejected.

On successful purchase:

buyer.balance -= car.price

seller.balance += car.price

This ensures transactional integrity between users.

📧 Email Notification (Celery + Redis)

When a car is purchased:

A Celery task is triggered.

Seller receives an email like:

"Your car has been purchased. The money has been transferred to your balance."

Celery runs asynchronously using Redis as a broker.

🚀 How to Run the Project
1️⃣ Clone repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup PostgreSQL

Create a database and update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5️⃣ Run migrations
python manage.py migrate

6️⃣ Run Redis

Make sure Redis server is running:

redis-server

7️⃣ Start Celery worker
celery -A your_project_name worker -l info

8️⃣ Run Django server
python manage.py runserver

🔐 Authentication

Users must be logged in to:

Create cars

Buy cars

Put cars on sale

Return cars from sale

🏗️ Architecture Overview

User → Django Views → Database (PostgreSQL)
↓
Celery Task
↓
Redis Broker
↓
Email Notification

🎯 What This Project Demonstrates

Django ORM relationships

Business logic separation

Balance validation

Celery asynchronous tasks

Redis integration

PostgreSQL usage

Ownership and state management

Basic marketplace logic
