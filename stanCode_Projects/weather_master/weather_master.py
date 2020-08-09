"""
File: weather_master.py
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
	This is a Temperature information processor,
	which allows users input their temperature information.
	At the end, it will show the highest and the lowest temperature.
	It also calculates the average temperature
	and the number of cold days, which represent the days under 16 degrees.
	"""
	print('stanCode "Weather Master 4.0"!')
	n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	highest = n
	lowest = n
	total = n
	times = 0
	cold = 0
	if n == EXIT:
		print('No temperature were entered.')
	else:
		if n < 16:
			cold = add_cold(cold)
		while True:
			n = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			times += 1
			# putting it here isn't that logical, while it could simplify the coding
			if n == EXIT:
				break
			elif n > highest:
				highest = n
				total = sum_temp(total, n)
				if n < 16:
					cold = add_cold(cold)
			elif n < lowest:
				lowest = n
				total = sum_temp(total, n)
				if n < 16:
					cold = add_cold(cold)
			else:
				total = sum_temp(total, n)
				if n < 16:
					cold = add_cold(cold)
		print('Highest temperature: ' + str(highest))
		print('Lowest temperature: ' + str(lowest))
		print('Average = ' + str(average(total, times)))
		print(str(cold) + ' cold day(s)')


def sum_temp(s, n):
	"""
	:param s: int, sum of total value of temperature
	:param n: int, latest information to add up
	:return: s + n
	"""
	s += n
	return s


def add_cold(c):
	"""
	:param c: int, temp < 16 and != -100
	:return: c + 1
	"""
	c += 1
	return c


def average(a, b):
	"""
	:param a: int, sum of total value
	:param b: int, the amount of temp information
	:return: a / b
	"""
	avg = a / b
	return avg


#
















###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
