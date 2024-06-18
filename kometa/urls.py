# kometa/urls.py

from django.urls import path
from kometa import views


app_name = "comet"
urlpatterns = [
    path('', views.index2, name='index'),
    path('comet/details/<int:comet_id>/', views.comet_details, name='comet_details'),
]
