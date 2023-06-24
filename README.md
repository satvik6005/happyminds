# happyminds
happyminds assignment elevator problem


data modelling:
	i have used redis for data managment as we hitting 
	database again and again in this project for which we 	
	require an in memory fast data management tool.
architecture:
	there is elevator object with following properities id  
	floor,operational,direction,door_open,requests.


 
api contracts:

	/elevators/initialize/:
	this is to initialize the n elevators it takes number of 	
	elevators as argument
	
	/elevators/:
	returns the list of all the elevators
	
	
	
	/run/:
	this is used to move from one floor to another it takes 
	in current and destination floor as argument and 			
	returns the most optimal elevator.

	/elevators/pk/maintenance/:
	marks elevator as operation or not operational

	/elevators/pk/door/open/:
	to open and close the elevator

	/elevators/pk/requests/:
	used to get the list of requests for an elevator

Note: above pk stands for primary key of an elevator.

deployment:
	for deployment clone the repository and use command docker-compose up

i have used a simple greedy algorithim to assign user elevators which works on minimum distance 
it assigns nearest operational elevator to the user.
maximum and minimum floors have been intialized by default.
	
	
