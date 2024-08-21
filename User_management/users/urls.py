from django.urls import path,include
from .views import * 
from django.contrib.auth import views as auth_views
# Create a router for the Admin User ViewSet

urlpatterns = [
    path('', register_view, name='register'),
    path('login/',login_view, name = 'login' ),
    path('home', home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]