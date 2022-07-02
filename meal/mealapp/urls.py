from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/', views.CustomerView.as_view()),
]
