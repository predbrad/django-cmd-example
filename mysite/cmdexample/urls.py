from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tail_log/', views.tail_log, name="tail_log"),

]