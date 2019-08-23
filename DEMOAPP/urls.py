from django.urls import path
from . import views

urlpatterns = [
    path('',views.hi, name='homepage'),
    path('add', views.add, name='add')
]