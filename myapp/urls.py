from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('getvideo/', views.getvideo, name="getvideo"),
    path('success/', views.success, name="success"),
    path('showmedia/', views.showmedia, name="showmedia"),
    path('allmedia/', views.allmedia, name="allmedia"),
    path('allmedia_success/', views.allmedia_success, name="allmedia_success"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
