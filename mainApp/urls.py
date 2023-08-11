from django.urls import path
from . import views

from mainApp.views import *
from django.urls import re_path as url

urlpatterns = [
    path('', views.index, name='index'),
    url('^csv-uploader/$', CsvUploader.as_view(), name='csv-uploader'),
]
