from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import APIView

import math

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
    set1 = HistoryTemprature.objects.all()
    set2 = HistorySoil.objects.all()
    set3 = HistoryLight.objects.all()
    set4 = HistoryAirHumidity.objects.all()
    queryset = set1, set2, set3, set4
    serializer_class = LastestInfoSerializer

class ControlDeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.filter(name='device 1')
    serializer_class = DeviceSerializer


@api_view(['GET'])
def getLastdata(request):
    data = []
    temp = HistoryTemprature.objects.latest('time')
    temp_serializer = HistoryTempratureSerializer(temp, many=False)

    soil = HistorySoil.objects.latest('time')
    soil_serializer = HistorySoilSerializer(soil, many=False)

    light = HistoryLight.objects.latest('time')
    light_serializer = HistoryLightSerializer(light, many=False)

    air = HistoryAirHumidity.objects.latest('time')
    air_serializer = HistoryAirHumiditySerializer(air, many=False)

    data = {'air': air_serializer.data, 'temprature': temp_serializer.data, 'soil': soil_serializer.data, 'light': light_serializer.data}
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

from datetime import datetime, date

@api_view(['GET'])
def getTodayData(request):
    today = datetime.now()
    
    airs = HistoryAirHumidity.objects.all()
    ret_air = filter(lambda y: today.date() == y.time.date(), airs)
    # air = filter(lambda y: y.time.hour % 2 == 0, ret_air)
    air_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for t in ret_air:
        is_call = 0
        index = math.floor(t.time.hour / 2)
        if air_data[index] != 0:
            is_call = 1
        air_data[index] += t.value
        if is_call:
            air_data[index] /= 2
    # air_serializer = HistoryAirHumiditySerializer(air, many=True)
    
    temps = HistoryTemprature.objects.all()
    ret_temp = filter(lambda y: today.date() == y.time.date(), temps)
    # temp = filter(lambda y: y.time.hour % 2 == 0, ret_temp)
    temp_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for t in ret_temp:
        is_call = 0
        index = math.floor(t.time.hour / 2)
        if temp_data[index] != 0:
            is_call = 1
        temp_data[index] += t.value
        if is_call:
            temp_data[index] /= 2
    # temp_serializer = HistoryTempratureSerializer(temp, many=True)
    
    soils = HistorySoil.objects.all()
    ret_soil = filter(lambda y: today.date() == y.time.date(), soils)
    # soil = filter(lambda y: y.time.hour % 2 == 0, ret_soil)
    soil_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for t in ret_soil:
        is_call = 0
        index = math.floor(t.time.hour / 2)
        if soil_data[index] != 0:
            is_call = 1
        soil_data[index] += t.value
        if is_call:
            soil_data[index] /= 2
    # soil_serializer = HistorySoilSerializer(soil, many=True)
    
    lights = HistoryLight.objects.all()
    ret_light = filter(lambda y: today.date() == y.time.date(), lights)
    # light = filter(lambda y: y.time.hour % 2 == 0, ret_light)
    light_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for t in ret_light:
        is_call = 0
        index = math.floor(t.time.hour / 2)
        if light_data[index] != 0:
            is_call = 1
        light_data[index] += t.value
        if is_call:
            light_data[index] /= 2
    # light_serializer = HistoryLightSerializer(light, many=True)
    
    data = {'air': air_data, 'temprature': temp_data, 'soil': soil_data, 'light': light_data}
    
    return Response(data)

import time, threading
def autoUpdate(i):
    starttime = time.time()
    while i:
        # Remove the Time taken by code to execute
        temp = HistoryTemprature.objects.latest('time')
        soil = HistorySoil.objects.latest('time')
        light = HistoryLight.objects.latest('time')
        air = HistoryAirHumidity.objects.latest('time')
        
        # no ok, need water
        if soil.value < 70 or air.value < 70:
            device = Device.objects.filter(name='water')
            # serializer = DeviceSerializer(data=data)
            if device and device[0].state == 0:
                device.update(state=1)
            # elif device and device[0].state == 1:
            #     break
        # ok, no more water
        else:
            device = Device.objects.filter(name='water')
            if device and device[0].state == 1:
                device[0].state = 0
            # elif device and device[0].state == 0:
            #     break
        print(device[0].state)
            
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))

class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.isloop = False
    
    def loop(self):
        starttime = time.time()
        while self.isloop:
            # Remove the Time taken by code to execute
            temp = HistoryTemprature.objects.latest('time')
            soil = HistorySoil.objects.latest('time')
            light = HistoryLight.objects.latest('time')
            air = HistoryAirHumidity.objects.latest('time')
            
            # no ok, need water
            if soil.value < 70 or air.value < 70:
                device = Device.objects.filter(name='water')
                # serializer = DeviceSerializer(data=data)
                if device and device[0].state == 0:
                    device.update(state=1)
                # elif device and device[0].state == 1:
                #     break
            # ok, no more water
            else:
                device = Device.objects.filter(name='water')
                if device and device[0].state == 1:
                    device[0].state = 0
                # elif device and device[0].state == 0:
                #     break
            print(device[0].name, device[0].state)
                
            time.sleep(1.0 - ((time.time() - starttime) % 1.0))

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


thread = StoppableThread()
@api_view(['GET', 'POST'])
def autoDevice(request):
    # thread.stop_event.set()
    # thread = StoppableThread(target=autoUpdate)
    # thread.name = 'thread'
    if request.method == 'GET':
        # thread.loop(False)
        # for threads in thread:
        # thread.loop(False)
        thread.isloop = False
        thread.loop()
        return Response('off')
    elif request.method == 'POST':
        # thread = StoppableThread(target=autoUpdate(True))
        # thread.start()
        thread.isloop = True
        thread.loop()
        return Response('on')