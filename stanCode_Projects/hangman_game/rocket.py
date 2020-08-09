"""
File: rocket.py
Name: Max Chang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SIZE = 10		# The size of the rocket


def main():
	rocket_head()
	rocket_coupler()
	rocket_body_upper()
	rocket_body_lower()
	rocket_coupler()
	rocket_head()

def rocket_head():
	"""
	This function will print the rocket head in the console
	:return: None
	"""
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ', end='')		# print empty string
		for k in range(i+1):
			print('/', end='')		# print /
		for k in range(i+1):
			print('\\', end='')		# print \
		print('')


def rocket_coupler():
	"""
	This function will print the rocket coupler in the console
	:return: None
	"""
	print('+', end='')
	for i in range(SIZE*2):
		print('=', end='')
	print('+')


def rocket_body_upper():
	"""
	This function will print the rocket upper body in the console
	:return: None
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(SIZE-(i+1)):
			print('.', end='')			# print .
		for k in range(i+1):
			print('/', end='')			# print /\
			print('\\', end='')
		for j in range(SIZE-(i+1)):
			print('.', end='')			# print .
		print('|')


def rocket_body_lower():
	"""
	This function will print the rocker lower body in the console
	:return: None
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')			# print .
		for k in range(SIZE-i):
			print('\\', end='')			# print \/
			print('/', end='')
		for j in range(i):
			print('.', end='')			# print .
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == "__main__":
	main()
