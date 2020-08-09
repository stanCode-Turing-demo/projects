"""
File: largest_digit.py
Name: Josephine
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

largest_dig = 0


def main():
	"""
	This program recursively finds and then prints the biggest digit in 5 different integers
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	This function will call the helper function to achieve the final goal.
	:param n: int, the integer
	:return: int, the biggest digit in the integer
	"""
	global largest_dig
	largest_dig = 0
	# Make sure that the integer is a positive integer.
	if n < 0:
		n *= -1
	find_largest_digit_helper(n)
	return largest_dig


def find_largest_digit_helper(n):
	"""
	The helper function which recursively gets each digit in the integer and compare with the former one.
	:param n: int, the integer
	:return: nothing / the function only records the biggest digit into the 'largest_digit' variable.
	"""
	global largest_dig
	# Base-Case
	if n == 0:
		return
	else:
		# Get each digit in n and compare it with the current biggest digit.
		if n % 10 > largest_dig:
			largest_dig = n % 10
		# Recursion
		find_largest_digit_helper(n//10)


if __name__ == '__main__':
	main()
