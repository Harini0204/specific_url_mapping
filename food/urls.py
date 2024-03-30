from django.urls import path
from food.views import *

app_name='haripriya'
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani'),
]