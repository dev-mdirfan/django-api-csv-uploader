from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mainApp.views import *


router = routers.DefaultRouter()

#API
router.register(r'students', StudentsViewSet, basename='students')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    path('', include('mainApp.urls'), name='mainApp'),
]
