from django.urls import path
from .views import *

urlpatterns = [
    path('',store,name="store"),
    path('about/',about,name="about"),
    path('sweets/',sweets,name="sweets"),
    path('cakes/',cakes,name="cakes"),
    path('chocolates/',chocolates,name="chocolates"),
    path('product/<str:id>/',productDetail,name="product_detail"),
    path('cart/',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('update_item/',updateItem,name="update_item"),
    path('process_order/',processOrder,name="process_order"),

]