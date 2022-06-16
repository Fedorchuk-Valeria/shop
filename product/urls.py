from django.urls import path
from .views import *

urlpatterns = [
    path('new/product', AddProductController.as_view(), name='add_product')
]
