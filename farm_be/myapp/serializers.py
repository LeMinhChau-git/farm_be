from rest_framework import serializers
from .models import Users
from .models import Temprature, SoilMoisure, LightIntensitive, AirHumidity
from .models import Device, Schedule
from .models import Notification, Threshold
from .models import HistoryTemprature, HistorySoil, HistoryLight, HistoryAirHumidity



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'password', 'role']

class TempratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temprature
        fields = ['id', 'current', 'high', 'medium', 'low']

class SoilMoisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilMoisure
        fields = ['id', 'current', 'high', 'medium', 'low']

class LightIntensitiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightIntensitive
        fields = ['id', 'current', 'high', 'medium', 'low']

class AirHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirHumidity
        fields = ['id', 'current', 'high', 'medium', 'low']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name', 'state', 'description']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'device', 'start', 'end', 'date', 'description']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'time', 'content', 'state']

class ThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threshold
        fields = ['id', 'name', 'value', 'description']

class HistorySoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorySoil
        fields = ['id', 'time', 'value']

class HistoryTempratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTemprature
        fields = ['id', 'time', 'value']

class HistoryLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryLight
        fields = ['id', 'time', 'value']

class HistoryAirHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryAirHumidity
        fields = ['id', 'time', 'value']