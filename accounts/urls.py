from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("sign-up/", views.signUp, name="sign-up"),
]