from rest_framework import viewsets, status,views
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.cache import cache
from .serializers import ElevatorSerializer
from .models import Elevator


max_floor=10
min_floor=-1
class eleveator_run(views.APIView):
    def post(self,request):
        try:
            
            curr_floor=request.data.get('current_floor')
            dest_floor=request.data.get('destination')
            if curr_floor>max_floor or dest_floor>max_floor or curr_floor<min_floor or dest_floor<min_floor:
                raise ValueError('destination or current floor out of range')
            elif len(cache.keys('elevator:*')) is 0:
                raise ValueError('elevators not initialized')
            dist=float('inf')
            res=None
            for i in cache.keys('elevator:*'):
                elevator = cache.get(i)
                serializer = ElevatorSerializer(elevator)
                print(serializer.data)
                if serializer.data["operational"]==True and serializer.data["running"]==False and abs(serializer.data["floor"]-curr_floor)<=dist:
                    dist=abs(serializer.data["floor"]-curr_floor)
                    res=serializer.data["id"]
            print(f"elevator coming to {curr_floor} floor")
            print('-----opening door-----')
            print('---------closing the door---')
            print(f'going to floor {dest_floor}')
            print('---reached----')
            print(res)
            
            
        
            chosen=cache.get(f"elevator:{res}")
            print(chosen)
            chosen.floor=dest_floor
            print(chosen.requests)
            chosen.requests.append(dest_floor)
            cache.set(f"elevator:{res}",chosen)
            
            
            print(res)
            return Response({"success":res},status=200)
        except Exception as e:
            return Response({'error':e},status=400)
        
   






class ElevatorViewSet(viewsets.ViewSet):
    #api for initializing all the elevators all the elevators
    @action(detail=False, methods=['post'])
    def initialize(self, request):
        num_elevators = int(request.data.get('num_elevators', 1))
        for i in range(num_elevators):
            elevator = Elevator(i)
            cache.set(f"elevator:{i}", elevator)

        return Response(status=status.HTTP_200_OK)
    
    #api for listing all the elevators
    def list(self, request):
        elevator_data = []
        for key in cache.keys('elevator:*'):
            elevator = cache.get(key)
            serializer = ElevatorSerializer(elevator)
            elevator_data.append(serializer.data)

        return Response(elevator_data)
    #api for retriving the specific elevator
    def retrieve(self, request, pk=None):
        elevator = cache.get(f"elevator:{pk}")
        if elevator is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ElevatorSerializer(elevator)
        return Response(serializer.data)
    #api for listing all the requests for a specific elevator
    @action(detail=True, methods=['get'])
    def requests(self, request, pk=None):
        elevator = cache.get(f"elevator:{pk}")
        if elevator is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(elevator.requests)

    
    

    

        return Response(status=status.HTTP_200_OK)
    #api for altering maintenance of an elevator
    @action(detail=True, methods=['put'])
    def maintenance(self, request, pk=None):
        elevator = cache.get(f"elevator:{pk}")
        if elevator is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        elevator.operational = bool(request.data.get('operational', True))
        cache.set(f"elevator:{pk}", elevator)

        return Response(status=status.HTTP_200_OK)
    #api for opening and closing door
    @action(detail=True, methods=['put'])
    def door(self, request, pk=None):
        elevator = cache.get(f"elevator:{pk}")
        if elevator is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        action = request.data.get('action')
        if action == 'open':
            elevator.door_open = True
        elif action == 'close':
            elevator.door_open = False
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        cache.set(f"elevator:{pk}", elevator)

        return Response(status=status.HTTP_200_OK)
