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

from django.urls import path, include
from rest_framework.routers import DefaultRouter
import mainapp.views as mainhapp

router = DefaultRouter()

router.register(r'user_requests', mainhapp.UserRequestViewSet, basename='user_requests')
router.register(r'segments', mainhapp.SegmentViewSet, basename='segments')

app_name = 'mainapp'

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('history/', mainhapp.history, name='history'),
]
