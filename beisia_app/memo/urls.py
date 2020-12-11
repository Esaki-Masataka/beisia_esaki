from django.urls import path
from . import views

app_name = 'memo'
urlpatterns = [
    path('create', views.ListsCreateView.as_view(), name='create'),    
    path('create/<int:year>/<int:month>/<int:day>/', views.ListsCreateView.as_view(), name='create'),
    path('thanks', views.thanks, name='thanks'),
    path('record', views.index, name='record'),
    path('okaimono/<int:num>', views.okaimono, name='okaimono'),
]
