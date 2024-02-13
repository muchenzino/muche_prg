from django.urls import path

from . import views

urlpatterns = [
    path('cisla', views.generate_random_number),
]