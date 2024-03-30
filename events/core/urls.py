from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("events/day", views.day, name="day"),
    path("events/week", views.week, name="week"),
    path("events/month", views.month, name="month"),
    path("generate", views.generate, name="generate"),
    path("events/", views.events, name="events"),
    path("login", views.login_view, name="login")
]