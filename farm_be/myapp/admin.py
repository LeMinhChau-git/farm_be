from django.contrib import admin
from .models import Init
from .models import Users
from .models import Temprature, SoilMoisure, LightIntensitive, AirHumidity
from .models import Device, Schedule
from .models import Notification, Threshold
from .models import HistoryTemprature, HistorySoil, HistoryLight, HistoryAirHumidity


@admin.register(Init)
class InitModel(admin.ModelAdmin):
    list_filter = ('email', 'password')
    list_display = ('email', 'password')

@admin.register(Users)
class UserModel(admin.ModelAdmin):
    list_filter = ('username', 'password', 'role')
    list_display = ('username', 'password', 'role')

@admin.register(Temprature)
class UserModel(admin.ModelAdmin):
    list_filter = ('current', 'high', 'medium', 'low')
    list_display = ('current', 'high', 'medium', 'low')

@admin.register(SoilMoisure)
class UserModel(admin.ModelAdmin):
    list_filter = ('current', 'high', 'medium', 'low')
    list_display = ('current', 'high', 'medium', 'low')

@admin.register(LightIntensitive)
class UserModel(admin.ModelAdmin):
    list_filter = ('current', 'high', 'medium', 'low')
    list_display = ('current', 'high', 'medium', 'low')

@admin.register(AirHumidity)
class UserModel(admin.ModelAdmin):
    list_filter = ('current', 'high', 'medium', 'low')
    list_display = ('current', 'high', 'medium', 'low')

@admin.register(Device)
class UserModel(admin.ModelAdmin):
    list_filter = ('name', 'state', 'description')
    list_display = ('name', 'state', 'description')

@admin.register(Schedule)
class UserModel(admin.ModelAdmin):
    list_filter = ('device', 'start', 'end', 'date', 'description')
    list_display = ('device', 'start', 'end', 'date', 'description')

@admin.register(Notification)
class UserModel(admin.ModelAdmin):
    list_filter = ('time', 'content', 'state')
    list_display = ('time', 'content', 'state')

@admin.register(Threshold)
class UserModel(admin.ModelAdmin):
    list_filter = ('name', 'value', 'description')
    list_display = ('name', 'value', 'description')

@admin.register(HistoryTemprature)
class UserModel(admin.ModelAdmin):
    list_filter = ('time', 'value')
    list_display = ('time', 'value')

@admin.register(HistorySoil)
class UserModel(admin.ModelAdmin):
    list_filter = ('time', 'value')
    list_display = ('time', 'value')

@admin.register(HistoryLight)
class UserModel(admin.ModelAdmin):
    list_filter = ('time', 'value')
    list_display = ('time', 'value')

@admin.register(HistoryAirHumidity)
class UserModel(admin.ModelAdmin):
    list_filter = ('time', 'value')
    list_display = ('time', 'value')