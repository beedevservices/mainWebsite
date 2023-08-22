from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from adminApp import views as app_views
from coreApp import views as app_views
from customerApp import views as app_views
from orderApp import views as app_views

urlpatterns = [
    path('', include('coreApp.urls')),
    path('admin/', admin.site.urls),
    path('client/', include('customerApp.urls')),
    path('invoice/', include('orderApp.urls')),
    path('private/', include('adminApp.urls')),
]
