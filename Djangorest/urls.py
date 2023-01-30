"""Djangorest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Djangorestapp import views
from django.urls import include, path
from rest_framework import routers
# router =routers.DefaultRouter()
# # router.register('api',views,EmployeeSWamyCBV,base_name='api')
# router.register('api',views,EmployeeSWamyCBV)
#...
from rest_framework.routers import DefaultRouter

#it is just viewset
router = DefaultRouter()
router.register('api',views.CricketerViewset,basename='cricket')


#model viewset..
router = DefaultRouter()
router.register('Modelapi',views.CricketModelviewset,basename='cricket')

#...


urlpatterns = [
    path('', include('Djangorestapp.urls')),
    path('admin/', admin.site.urls),
    path('viewset/',include(router.urls)), #viewset..
    path('modelviewset/',include(router.urls)), #modelviewset.
    #authentication
    path('auth/',include('rest_framework.urls',namespace='rest_framwork')), #modelviewset.


]