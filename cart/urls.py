from django.urls import path
from .import views

urlpatterns = [
  path('add-to-cart', views.add_to_cart_view, name="add_to_cart_view"),
  path('my-cart', views.my_cart_view, name="my_cart_view"),
  path('delete_cart_view/<int:cart_id>', views.delete_cart_view_item, name="delete_cart_view_item")
]
