from django.db import models

# Create your models here.


class Elevator:
    def __init__(self, elevator_id):
        self.id = elevator_id
        self.floor = 0
        self.direction = 'stop'
        self.door_open = False
        self.running = False
        self.operational = True
        self.requests = []

    def __str__(self):
        return f"Elevator {self.id}"

