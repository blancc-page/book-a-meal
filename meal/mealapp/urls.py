from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/users/', views.UsersView.as_view()),
    path('api/v1/caterers/', views.CatererView.as_view()),
    path('api/v1/users/', views.CustomerView.as_view()),
]
