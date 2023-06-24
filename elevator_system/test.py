import requests

BASE_URL = 'http://localhost:8080'

# Initialize the elevator system with 3 elevators
num_elevators = 5
elevator_id=2
initialize_url = f'{BASE_URL}/elevators/initialize/'
initialize_data = {'num_elevators': num_elevators}
response = requests.post(initialize_url, data=initialize_data)
if response.status_code == 200:
    print(f'Elevator system initialized with {num_elevators} elevators.')
else:
    print('Failed to initialize the elevator system.')

# Get the list of all elevators
elevators_url = f'{BASE_URL}/elevators/'
response = requests.get(elevators_url)
if response.status_code == 200:
    elevators = response.json()
    print('List of elevators:')
    for elevator in elevators:
        print(elevator)
else:
    print('Failed to retrieve the list of elevators.')



# Get the list of requests for elevator 0
requests_url = f'{BASE_URL}/elevators/{elevator_id}/requests/'
response = requests.get(requests_url)
if response.status_code == 200:
    requests = response.json()
    print(f'List of requests for elevator {elevator_id}:')
    for request in requests:
        print(request)
else:
    print(f'Failed to retrieve the list of requests for elevator {elevator_id}.')



# Mark elevator 0 as not operational
maintenance_url = f'{BASE_URL}/elevators/{elevator_id}/maintenance/'
maintenance_data = {'operational': False}
response = requests.put(maintenance_url, data=maintenance_data)
if response.status_code == 200:
    print(f'Elevator {elevator_id} marked as not operational.')
else:
    print(f'Failed to mark elevator {elevator_id} as not operational.')

# Open the door for elevator 0
door_url = f'{BASE_URL}/elevators/{elevator_id}/door/open/'
response = requests.put(door_url)
if response.status_code == 200:
    print(f'Door of elevator {elevator_id} opened.')
else:
    print(f'Failed to open the door of elevator {elevator_id}.')

# Close the door for elevator 0
door_url = f'{BASE_URL}/elevators/{elevator_id}/door/close/'
response = requests.put(door_url)
if response.status_code == 200:
    print(f'Door of elevator {elevator_id} closed.')
else:
    print(f'Failed to close the door of elevator {elevator_id}.')
