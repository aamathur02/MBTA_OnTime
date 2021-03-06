import requests
import json
from datetime import datetime as dt

'''
Simple python script to acess the MBTA api and return a json. 
'''

#function makes API call to get a list of valid line names 
#this line list will be used to check if user input is valid
def create_lines_list(base_url):

	#set header and parametrs for make_API_Request method params
	headers = {
    'accept': 'application/vnd.api+json',
	}

	#filter routes endpoint to only include Commuter Rail routes
	params = (
    ('filter[type]', '2'),
	)

	line_response = make_API_Request(base_url, "routes", headers, params)
	line_list = []
	for i in range(len(line_response)):
		line_list.append((line_response[i]['id'], (line_response[i]['attributes']['long_name'])))

	return line_list

#method to take create a list of all stops on a certain Commuter Rail Line
#@pa
def create_stops_list(line_id, base_url):

	headers = {
    'accept': 'application/vnd.api+json',
	}

	params = (
    ('filter[route]', line_id),
	)

	stop_response  = make_API_Request(base_url, "stops", headers, params)
	stop_list = []

	for i in range(len(stop_response)):
		stop_list.append(stop_response[i]['attributes']['name'])
		print(stop_response[i]['attributes']['name'])

	return stop_list

def find_travel_direction(beginning, ending):

	#print(f"Start Index: {begin_index}")
	#print(f'End Index: {end_index}')

	if beginning == ending:
		print("You have chosen the same stop to get on and off at:")
	elif beginning < ending:
		return 1
	else:
		return 0

def find_trips(base_url, direction_id, start_time, line_name, beginning_stop):

	headers = {
    'accept': 'application/vnd.api+json',
	}

	params = (
	('page[limit]', '3'),
    ('sort', 'arrival_time'),
    ('filter[direction_id]', direction_id),
    ('filter[min_time]', start_time),
    ('filter[route]', line_name),
    ('filter[stop]', beginning_stop),
	)

	print(beginning_stop)

	trip_response = make_API_Request(base_url, "schedules", headers, params)
	trip_list = []
	for i in range(len(trip_response)):
		trip_list.append(trip_response[i]['relationships']['trip']['data']['id'])
		#print(trip_response[i]['relationships']['trip']['data']['id'])


	return trip_list


def find_times(base_url,trip_list, beginning_stop, ending_stop):

	headers = {
    'accept': 'application/vnd.api+json',
	}


	begin_times = []
	end_times = []
	for i in range(len(trip_list)):

		params = (
    	('filter[trip]', trip_list[i]),
		)	

		time_reponse = make_API_Request(base_url, 'schedules', headers, params)

		for k in range(len(time_reponse)):
			if time_reponse[k]['relationships']['stop']['data']['id'] == beginning_stop:
				base_time = time_reponse[k]['attributes']['arrival_time']
				print(base_time)
				begin_times.insert(i, base_time[base_time.index("T") +1 : base_time.index("T")+6])
			elif time_reponse[k]['relationships']['stop']['data']['id'] == ending_stop:
				base_time = time_reponse[k]['attributes']['arrival_time']
				print(base_time)
				end_times.insert(i, base_time[base_time.index("T") +1 : base_time.index("T")+6])

	return begin_times, end_times

#base function to make all API requests
#used to make the process of making API request abstract
def make_API_Request(url, end_tag, head, params):

	request_url = url + "/" + end_tag

	base_response = requests.get(request_url, headers = head, params = params)
	response = json.loads(base_response.text)

	if base_response.status_code == 200:
		return response['data']

def main():
	#base url from which we can access the api
	base_url = "https://api-v3.mbta.com"

	lines = create_lines_list(base_url)

	direction_id: {"Outbound": 0 , "Inbound": 1}


	line_name = input("Please Enter a Commuter Rail Line Name: ")

	if line_name not in lines:
		print("Invalid Line Name, Please run again\n")

	stops = create_stops_list(line_name, base_url)

	starting_stop = input("Please Enter the Starting Stop:\n")

	ending_stop = input("Please Enter the Ending Stop:\n")

	if str(starting_stop) not in stops or str(ending_stop) not in stops:
		print("Invalid Stops")

	direction = find_travel_direction(stops, starting_stop, ending_stop)

	begin_time = input("When would you like to leave (Please enter as 24 hour time in format HH:MM):\n")

	trips = find_trips(base_url, direction, begin_time, line_name, starting_stop)

	times = find_times(base_url, trips, starting_stop, ending_stop)

	print("Your Options Are:\n")
	for i in range(len(times[0])):
		print(f"Get on at {starting_stop} at {times[0][i]} and get off at {ending_stop} at {times[1][i]} ")
	

#main()

