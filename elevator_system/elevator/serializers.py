from rest_framework import serializers

from django.core.cache import cache

class ElevatorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    floor = serializers.IntegerField()
    direction = serializers.ChoiceField(choices=[('up', 'Up'), ('down', 'Down'), ('stop', 'Stop')])
    door_open = serializers.BooleanField()
    running = serializers.BooleanField()
    operational = serializers.BooleanField()
    requests = serializers.ListField(child=serializers.IntegerField(), read_only=True)

        
