from django.urls import path
from getimage import views


urlpatterns = [
    path("", views.home, name="home"),
]