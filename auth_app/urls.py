from django.urls import path
from auth_app import views

app_name = 'auth_app'

urlpatterns = [
    path('register', views.registration, name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    path('success', views.login_success, name="login_success"),
    path('register-success', views.register_success, name="registration_success")
]
