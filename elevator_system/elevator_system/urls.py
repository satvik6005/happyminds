from django.urls import path, include
from rest_framework import routers
from elevator.viewsets import ElevatorViewSet,eleveator_run

router = routers.DefaultRouter()
router.register(r'elevators', ElevatorViewSet, basename='elevator')

urlpatterns = [
    path('run/',eleveator_run.as_view(),name='run'),
    path('', include(router.urls)),
    
]