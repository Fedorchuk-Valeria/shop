from django.shortcuts import render, redirect
from django.views import View


class MainPageController(View):

    template_name = 'main_page/main.html'

    def get(self, request):
        return render(request, self.template_name)
