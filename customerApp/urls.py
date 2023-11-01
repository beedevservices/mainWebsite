from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls start with client/

urlpatterns = [
    path('', views.clientPortal),
    path('logReg/', views.clientLogReg),
    path('login/', views.clientLogin),
    path('reg/', views.clientReg),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)