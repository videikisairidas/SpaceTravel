# stars/urls.py

from django.urls import path
from stars import views


app_name = "stars"
urlpatterns = [
    path('', views.index2, name='index'),
    # path('star/details/<int:star_id>/', views.star_details, name='star_details'),
]
