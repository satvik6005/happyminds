import unittest
import requests

class ElevatorTestCase(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:8000'
        self.headers = {'Content-Type': 'application/json'}

    def test_initialize_elevators(self):
        num_elevators = 5
        url = f'{self.base_url}/elevators/initialize/'
        data = {'num_elevators': num_elevators}

        response = requests.post(url, json=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to verify the response data or database state

    def test_get_all_elevators(self):
        url = f'{self.base_url}/elevators/'

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to verify the response data

    def test_move_elevator(self):
        current_floor = 1
        destination_floor = 5
        url = f'{self.base_url}/run/'
        data = {'current_floor': current_floor, 'destination': destination_floor}

        response = requests.post(url, json=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to verify the response data

    def test_mark_elevator_maintenance(self):
        elevator_id = 1
        url = f'{self.base_url}/elevators/{elevator_id}/maintenance/'
        data={"operational": 0}

        response = requests.put(url,json=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to verify the response data or database state

    def test_open_elevator_door(self):
        elevator_id = 1
        url = f'{self.base_url}/elevators/{elevator_id}/door/'
        data={"action":"close"}

        response = requests.put(url,json=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to verify the response data or database state

    def test_get_elevator_requests(self):
        elevator_id = 1
        url = f'{self.base_url}/elevators/{elevator_id}/requests/'

        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        # Add additional assertions to verify the response data

if __name__ == '__main__':
    unittest.main()
