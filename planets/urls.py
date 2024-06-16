from django.urls import path
from planets import views


app_name = "planets"
urlpatterns = [
    path('', views.index, name='index'),
    # path('<slug:planet>', views.planet, name='planet'),
    # path('comet/details/<int:comet_id>/', views.comet_details, name='comet_details'),
]
