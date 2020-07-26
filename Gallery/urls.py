from django.contrib import admin
from django.urls import path, include
from .views import Gallery

urlpatterns = [
    path('', Gallery.as_view(), name='Gallery')
]