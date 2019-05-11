from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/dataChannel', views.data_channel, name='dataChannel'),
]