from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.mIndex),
    path('tabs/', views.tabMenus),
    path('hidden/', views.hiddenMenus),
    path('sidebars/', views.sidebarMenus),
    path('sticky/', views.stickyMenus),
    path('dropdowns/', views.dropdowns),
]