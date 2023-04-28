from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import APIView


from rest_framework import generics
from rest_framework import mixins


from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import Users
from .models import Temprature, SoilMoisure, LightIntensitive, AirHumidity
from .models import Device, Schedule
from .models import Notification, Threshold
from .models import HistoryTemprature, HistorySoil, HistoryLight, HistoryAirHumidity

from .serializers import UsersSerializer
from .serializers import TempratureSerializer, SoilMoisureSerializer, LightIntensitiveSerializer, AirHumiditySerializer
from .serializers import DeviceSerializer, ScheduleSerializer
from .serializers import NotificationSerializer, ThresholdSerializer
from .serializers import HistoryTempratureSerializer, HistorySoilSerializer, HistoryLightSerializer, HistoryAirHumiditySerializer
from .serializers import LastestInfoSerializer



class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class TempratureViewSet(viewsets.ModelViewSet):
    queryset = Temprature.objects.all()
    serializer_class = TempratureSerializer

class SoilMoisureViewSet(viewsets.ModelViewSet):
    queryset = SoilMoisure.objects.all()
    serializer_class = SoilMoisureSerializer

class LightIntensitiveViewSet(viewsets.ModelViewSet):
    queryset = LightIntensitive.objects.all()
    serializer_class = LightIntensitiveSerializer

class AirHumidityViewSet(viewsets.ModelViewSet):
    queryset = AirHumidity.objects.all()
    serializer_class = AirHumiditySerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class ThresholdViewSet(viewsets.ModelViewSet):
    queryset = Threshold.objects.all()
    serializer_class = ThresholdSerializer

class HistoryTempratureViewSet(viewsets.ModelViewSet):
    queryset = HistoryTemprature.objects.all()
    serializer_class = HistoryTempratureSerializer

class HistorySoilViewSet(viewsets.ModelViewSet):
    queryset = HistorySoil.objects.all()
    serializer_class = HistorySoilSerializer

class HistoryLightViewSet(viewsets.ModelViewSet):
    queryset = HistoryLight.objects.all()
    serializer_class = HistoryLightSerializer

class HistoryAirHumidityViewSet(viewsets.ModelViewSet):
    queryset = HistoryAirHumidity.objects.all()
    serializer_class = HistoryAirHumiditySerializer

class LastestInfoViewSet(viewsets.ModelViewSet):
    queryset = HistoryTemprature.objects.last(), HistorySoil.objects.last(), HistoryLight.objects.last(), HistoryAirHumidity.objects.last()
    serializer_class = LastestInfoSerializer

class ControlDeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.filter(name='device 1')
    serializer_class = DeviceSerializer

# @api_view(['GET'])
# def 

@api_view(['GET'])
def getLastdata(request):
    data = []
    temp = HistoryTemprature.objects.all()
    serializer = HistoryTempratureSerializer(temp, many=True)
    data += [serializer.data[-1]]

    soil = HistorySoil.objects.all()
    serializer = HistorySoilSerializer(soil, many=True)
    data += [serializer.data[-1]]

    light = HistoryLight.objects.all()
    serializer = HistoryLightSerializer(light, many=True)
    data += [serializer.data[-1]]

    air = HistoryAirHumidity.objects.all()
    serializer = HistoryAirHumiditySerializer(air, many=True)
    data += [serializer.data[-1]]

    return Response(data)
    
@api_view(['GET', 'PUT', 'POST'])
def controlDevice(request):
    if request.method == 'PUT' or request.method == 'POST':
        data = JSONParser().parse(request)
        device = Device.objects.filter(name=data['name'])
        serializer = DeviceSerializer(data=data)
        # if serializer.is_valid():
        if device[0].state == 0:
            device.update(state=1)
        else:
            device.update(state=0)
        print(device[0])
        return JsonResponse(data, status=status.HTTP_200_OK)
        # return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        users = Device.objects.all()
        serializer = DeviceSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def getUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = UsersSerializer(data=data)
        users = Users.objects.all()
        if serializer.is_valid():
            for i in users:
                if i.username == data["username"] and i.password == data["password"]:
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
