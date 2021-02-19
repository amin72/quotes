from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    path('add_to_statistics/',
        views.AddToStatisticsAPIView.as_view(),
        name='add_to_statistics'),
]