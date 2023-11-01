from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from adminApp import views as app_views
from coreApp import views as app_views
from customerApp import views as app_views
from orderApp import views as app_views
from employeeApp import views as app_views

urlpatterns = [
    path('', include('coreApp.urls')),
    path('admin/', admin.site.urls),
    path('client/', include('customerApp.urls')),
    path('order/', include('orderApp.urls')),
    path('company/', include('adminApp.urls')),
    path('employee/', include('employeeApp.urls')),
]
