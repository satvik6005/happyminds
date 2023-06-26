from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.



class Elevator(models.Model):
    id=models.AutoField(primary_key=True)
    floor = models.IntegerField(default=0)
    door_open = models.BooleanField(default=False)
    running = models.BooleanField(default=False)
    operational = models.BooleanField(default=True)
    

    def __str__(self):
        return f"Elevator {self.id}"
class requests(models.Model):
    id=models.AutoField(primary_key=True)
    floor=models.IntegerField()
    elevator=models.ForeignKey(Elevator,on_delete=CASCADE)


