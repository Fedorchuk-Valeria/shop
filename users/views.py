from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User


class RegistrationController(View):
    template_name = 'users/seller_ registration.html'
    model_form = NewSellerForm

    def get(self, request):
        form = self.model_form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.model_form(request.POST)
        if form.is_valid():
            form.is_active = True
            form.save()
        else:
            mess = 'Try again'
            return render(request, self.template_name, {'form': form, 'mess': mess})
        return redirect('seller_profile')


class SignInController(View):
    template_name = 'users/authentication.html'
    model_form = AuthenticationForm

    def get(self, request):
        user = User()
        try:
            user = User.objects.get(is_active=True, is_superuser=False)
            user.is_active = False
            user.save()
            form = self.model_form
        except user.DoesNotExist:
            form = self.model_form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User()
        try:
            red_str = ''
            try:
                user = Seller.objects.get(username=username, password=password)
                red_str = 'seller_profile'
            except user.DoesNotExist:
                user = Client.objects.get(username=username, password=password)
                red_str = 'client_profile'
            user.is_active = True
            user.save()
            return redirect(red_str)
        except user.DoesNotExist:
            error_message = 'User not found'
            form = self.model_form
            f_d = {
                'form': form,
                'mess': error_message
            }
            return render(request, self.template_name, f_d)


class ProfileController(View):
    template_name = 'users/seller_profile.html'
    model = Seller

    def get(self, request):
        user = self.model.objects.get(is_active=True, is_superuser=False)
        return render(request, self.template_name, {'user': user})
