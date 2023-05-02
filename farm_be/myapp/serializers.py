from rest_framework import serializers
from .models import Users
from .models import Temprature, SoilMoisure, LightIntensitive, AirHumidity
from .models import Device, Schedule
from .models import Notification, Threshold
from .models import HistoryTemprature, HistorySoil, HistoryLight, HistoryAirHumidity
from .models import LastestInfo



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'role']

class TempratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temprature
        fields = ['current', 'high', 'medium', 'low']

class SoilMoisureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilMoisure
        fields = ['current', 'high', 'medium', 'low']

class LightIntensitiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LightIntensitive
        fields = ['current', 'high', 'medium', 'low']

class AirHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirHumidity
        fields = ['current', 'high', 'medium', 'low']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name', 'state', 'description']

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['device', 'start', 'end', 'date', 'description']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['time', 'content', 'state']

class ThresholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threshold
        fields = ['name', 'value', 'description']

class HistorySoilSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorySoil
        fields = ['time', 'value']

class HistoryTempratureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTemprature
        fields = ['time', 'value']

class HistoryLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryLight
        fields = ['time', 'value']

class HistoryAirHumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryAirHumidity
        fields = ['time', 'value']

class LastestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastestInfo
        fields = ['time', 'value']