from django.urls import path

from . import views

urlpatterns = [
    path('time', views.colorful_time),
]