from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('Logout', views.logout, name="logout "),
    path('Contact', views.contact, name="contact ")
]