from django.urls import path,include
from.views import *
from .views import home, add_resort, view_resort, view_customer, update_resort, view_bookings, delete_customer, delete_resort



urlpatterns = [
    path('',home,name='adm'),
    path('addresort/', add_resort, name='add_resort'),
    path('viewresort/',view_resort,name='view_resort'),
    path('viewcustomer/',view_customer,name='view_customer'),
    path('updateresort/<int:id>',update_resort,name='upadate_resort'),
    path('viewbookings/',view_bookings,name='view_bookings'),
    path('deletecustomer/<int:id>',delete_customer,name='delete_customer'),
    path('deleteresort/<int:id>',delete_resort,name='delete_resort'),
    
]