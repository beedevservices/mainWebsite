from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls start with employee/

urlpatterns = [
    path('', views.employeePortal),
    path('logReg/', views.employeeLogReg),
    # path('login/', views.adminLogin),
    # path('reg/', views.adminReg),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)