from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('codes', views.codes, name='codes'),
    path('add', views.addCodes, name='add')
]