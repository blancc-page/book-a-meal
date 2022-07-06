from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('api/v1/customers/', views.CustomerView.as_view()),
    path('accounts/profile/', views.ProfileView.as_view()),
    path('api-auth/', views.CustomAuthToken.as_view()),
    path('api/menu/', views.MenuView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)