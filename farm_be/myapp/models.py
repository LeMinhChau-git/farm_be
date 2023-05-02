from django.db import models


class Init(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.email

class Users(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.username

class Temprature(models.Model):
    current = models.FloatField()
    high = models.FloatField()
    medium = models.FloatField()
    low = models.FloatField()
    
    def __str__(self):
        return self.current

class SoilMoisure(models.Model):
    current = models.FloatField()
    high = models.FloatField()
    medium = models.FloatField()
    low = models.FloatField()
    
    def __str__(self):
        return self.current

class LightIntensitive(models.Model):
    current = models.FloatField()
    high = models.FloatField()
    medium = models.FloatField()
    low = models.FloatField()
    
    def __str__(self):
        return self.current

class AirHumidity(models.Model):
    current = models.FloatField()
    high = models.FloatField()
    medium = models.FloatField()
    low = models.FloatField()
    
    def __str__(self):
        return self.current

class Device(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    state = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    device = models.CharField(max_length=30)
    start = models.TimeField()
    end = models.TimeField()
    date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.device

class Notification(models.Model):
    time = models.DateTimeField(primary_key=True)
    content = models.TextField()
    state = models.IntegerField()
    
    def __str__(self):
        return self.time

class Threshold(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    value = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name

class HistoryTemprature(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.IntegerField()
    
    def __str__(self):
        return self.time

class HistorySoil(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.IntegerField()
    
    def __str__(self):
        return self.time

class HistoryLight(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.IntegerField()
    
    def __str__(self):
        return self.time

class HistoryAirHumidity(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.IntegerField()
    
    def __str__(self):
        return self.time

class LastestInfo(models.Model):
    time = models.DateTimeField(primary_key=True)
    value = models.IntegerField()
    
    def __str__(self):
        return self.time