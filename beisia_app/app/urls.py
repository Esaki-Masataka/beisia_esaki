from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('home/', views.index, name='home'),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
        ),
]# -*- coding: utf-8 -*-

