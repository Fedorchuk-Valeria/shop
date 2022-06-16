from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from users.models import Seller
from .models import Product


class AddProductController(View):

    template_name = 'product/new_product.html'
    model_form = NewProductForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.model_form})

    def post(self, request):
        form = self.model_form(request.POST)
        seller = Seller.objects.get(is_active=True)
        form.seller = seller
        if form.is_valid():
            form.save()
        else:
            mess = 'Try again'
            return render(request, self.template_name, {'form': form, 'mess': mess})
        return redirect('user_profile')
