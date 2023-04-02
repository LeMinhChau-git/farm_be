from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UsersViewSet
from .views import TempratureViewSet, SoilMoisureViewSet, LightIntensitiveViewSet, AirHumidityViewSet
from .views import DeviceViewSet, ScheduleViewSet
from .views import NotificationViewSet, ThresholdViewSet
from .views import HistoryTempratureViewSet, HistorySoilViewSet, HistoryLightViewSet, HistoryAirHumidityViewSet

from .views import getUser

routers = DefaultRouter()
routers.register('users', UsersViewSet, basename='users')
routers.register('temprature', TempratureViewSet, basename='temprature')
routers.register('soil_moisure', SoilMoisureViewSet, basename='soil_moisure')
routers.register('light_intensitive', LightIntensitiveViewSet, basename='light_intensitive')
routers.register('air_humidity', AirHumidityViewSet, basename='air_humidity')
routers.register('device', DeviceViewSet, basename='device')
routers.register('schedule', ScheduleViewSet, basename='schedule')
routers.register('notification', NotificationViewSet, basename='notification')
routers.register('threshold', ThresholdViewSet, basename='threshold')
routers.register('history_temprature', HistoryTempratureViewSet, basename='history_temprature')
routers.register('history_soil', HistorySoilViewSet, basename='history_soil')
routers.register('history_light', HistoryLightViewSet, basename='history_light')
routers.register('history_air_humidity', HistoryAirHumidityViewSet, basename='history_air_humidity')


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('get_user/', getUser),
]
