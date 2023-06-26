from rest_framework import serializers
from .models import Elevator,requests


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ('id', 'floor',  'door_open', 'running', 'operational')
class requestsserializer(serializers.ModelSerializer):
    class Meta:
        model=requests
        fields=("id","floor","elevator")

        
