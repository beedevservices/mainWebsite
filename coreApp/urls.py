from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# All urls start with /

urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('about/', views.about),
    path('projects/', views.projects),
    path('contact/', views.contact),
    path('services/', views.services),
    # path('policies/terms/', views.termsOfUse),
    path('policies/cookies/', views.cookies),
    # path('policies/disclaimer/', views.disclaimer),
    # path('policies/linking/', views.linking),
    # path('policies/privacy/', views.privacy),
    # path('policies/refund/', views.refund),
    # path('careers/jobs/', views.jobs),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)