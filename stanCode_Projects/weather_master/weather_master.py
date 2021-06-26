"""
File: weather_master.py
Name: Claire Yang
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


EXIT = -100


def main():
	"""
	This program is to compute the highest, lowest, average, cold days among the weather data user inputs
	"""
	intro()
	weather_data_master()


def intro():
	"""This function wraps 1 print as intro()"""
	print('stanCode \"Weather Master 4.0\"!')


def weather_data_master():
	"""
	This function is to compute the highest, lowest, average, cold days among user inputs
	Highest temperature = the highest temperature among user inputs
	Lowest temperature = the lowest temperature among user inputs
	Average = sum of all temperatures / count of all temperatures
	Cold days = count of user inputs lower than 16
	"""
	# create records for accumulated data first: (line 39, 40, 41)
	sum_of_temperatures = 0
	count_of_temperatures = 0
	cold_days = 0
	data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		sum_of_temperatures += data
		count_of_temperatures += 1
		if data < 16:
			cold_days += 1
		# create the highest and lowest
		highest = data
		lowest = data
		# while True for the rest user inputs until user input equals to EXIT
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			sum_of_temperatures += data
			count_of_temperatures += 1
			if data < 16:
				cold_days += 1
			if data > highest:
				# If new data is higher:
				# the highest temperature will be replaced by the new data
				# the lowest temperature remains the same
				highest = data
			if data < lowest:
				# If new data is lower:
				# the highest temperature remains the same
				# the lowest temperature will be replaced by the new data
				lowest = data
		average_temperature = (sum_of_temperatures / count_of_temperatures)
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(average_temperature))
		print(str(cold_days) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
