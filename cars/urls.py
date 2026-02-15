from django.urls import path
from cars.views import (cars_create_view, cars_list_view,
                         car_update_view, car_detail_view, sales_page_view,
                         payment_view, sell_car_view)

urlpatterns = [
    path("create", cars_create_view),
    path("<int:pk>/update/", car_update_view),
    path('', cars_list_view),
    path("<int:car_id>/detail/", car_detail_view),
    path("sales/", sales_page_view),
    path("<int:car_id>/sell/", sell_car_view),
    path("<int:car_id>/buy/", payment_view)
]
