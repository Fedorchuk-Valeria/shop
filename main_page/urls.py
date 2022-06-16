from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPageController.as_view(), name='main')
]
