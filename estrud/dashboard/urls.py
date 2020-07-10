from django.urls import path
from .views import dashboard, settings


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('settings/', settings, name='settings'),
]
