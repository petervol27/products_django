from django.urls import path
from . import views

urlpatterns = [path("", views.show_products, name="products_list")]
