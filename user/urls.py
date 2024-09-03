# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('some-url/', views.some_view, name='some_view'),
]
