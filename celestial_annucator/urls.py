"""celestial_annucator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import celestial_annucator.views
from django.conf import settings
from django.conf.urls.static import static
from celestial_annucator.views import index, registration

urlpatterns = [
    path('auth/', include('authapp.urls', namespace='auth')),
    path('admin/', admin.site.urls),
    path('main/', include('mainapp.urls')),
    path('', index, name="index"),
    path('airports_by_term/', celestial_annucator.views.get_airports_by_term),
    path('flight_search/', celestial_annucator.views.flights_search)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)