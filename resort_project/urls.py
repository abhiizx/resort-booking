
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # assuming home app
    path('adminapp/', include('adminapp.urls')), # include adminapp urls
    path('account/', include('account.urls')),
    path('',include('account.urls')),
    path('user/', include('user.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

