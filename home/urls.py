from django.urls import path
from . import views
from .views import details_view
from .views import check_availability
from .views import booking_view

urlpatterns = [
    path('navbar/', views.navbar, name='navbar'),
    path('register/', views.register_view, name='register'), # Root URL for this app
    path('', views.login_page, name='login'),
    path('home/', views.home_view, name='home'),
    path('details/', details_view, name='details'),
    path('check_availability/<int:booking_id>/', check_availability, name='check_availability'),
    path('booking/', booking_view, name='booking'),
]
