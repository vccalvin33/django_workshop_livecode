from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/<str:task_id>/edit", views.edit, name="edit-task"),
    path("tasks/<str:task_id>/delete", views.delete, name="delete-task"),
    path("login/", views.login_user, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_user, name="logout"),
]