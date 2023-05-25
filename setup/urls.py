from django.contrib import admin
from django.urls import path, include
from portifolio import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portifolio.urls')),
]
