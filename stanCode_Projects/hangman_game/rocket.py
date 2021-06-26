"""
File: rocket.py
Name: Claire Yang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This program is to build a rocket
	The size of rocket is determined by a constant defined as SIZE at top of the file
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""This function is to build the head of the rocket"""
	for i in range(SIZE):
		for j in range(SIZE - i):
			print(' ', end='')
		for j in range(i + 1):
			print('/', end='')
		for j in range(i + 1):
			print('\\', end='')
		print("")


def belt():
	"""This function is to build the belt of the rocket"""
	print('+', end='')
	for i in range(SIZE * 2):
		print('=', end='')
	print('+', end='')
	print("")


def upper():
	"""This function is to build the upper body of the rocket"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(SIZE - (i + 1)):
			print('.', end='')
		for j in range(i + 1):
			print('/', end='')
			print('\\', end='')
		for j in range(SIZE - (i + 1)):
			print('.', end='')
		print('|', end='')
		print("")


def lower():
	"""This function is to build the lower body of the rocket"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(SIZE - i):
			print('\\', end='')
			print('/', end='')
		for j in range(i):
			print('.', end='')
		print('|', end='')
		print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()