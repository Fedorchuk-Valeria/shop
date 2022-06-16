from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('sign/', include('users.urls')),
    path('sign/profile/seller/', include('product.urls'))
]
