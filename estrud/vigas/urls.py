from django.urls import path
from .views import home, starter


urlpatterns = [
    path('', home, name='home'),
    path('starter/', starter, name='starter')
]
