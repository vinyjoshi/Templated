from django.contrib import admin
from django.urls import path, include
from .views import Home_view, Generic

urlpatterns = [
    path('', Home_view.as_view(), name='Home'),
    path('generic', Generic.as_view(), name='Generic'),
]