from django.urls import path
from .views import *
from .forms import NewClientForm
from .models import Client

urlpatterns = [
    path('up/seller', RegistrationController.as_view(), name='reg_seller'),
    path('up/client', RegistrationController.as_view(template_name='users/client_registration.html',
                                                     model_form=NewClientForm), name='reg_client'),
    path('in', SignInController.as_view(), name='authentication'),
    path('profile/user', ProfileController.as_view(), name='seller_profile'),
    path('profile/user', ProfileController.as_view(template_name='users/client_profile.html', model=Client),
         name='client_profile')
]
