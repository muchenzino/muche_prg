from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.models_list),
]