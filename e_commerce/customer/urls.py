from django.urls import path
from . import views

urlpatterns=[
    path('home',views.customer_home),
    path('password',views.change_password),
    path('order',views.my_order),
    path('product',views.product_details),
    path('profile',views.profile),
    path('cart',views.view_cart)
]
