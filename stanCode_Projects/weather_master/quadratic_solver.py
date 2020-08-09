"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	The codes following are asking users to input a, b, c respectively
	to compute the roots of equation ax^2 + bx + c = 0.
	At the end, it would come up with three types of answer,
	one root, two roots and no real roots.
	"""
	print('stanCode Quadratic Solver!')

	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	
	y = b * b - 4 * a * 		# the discriminant
	z = 2 * a
	
	# one root
	if y == 0:
		x = (-b + math.sqrt(y)) / z
		print('One root: ' + str(x))
	# twu roots
	elif y > 0:
		x = (-b + math.sqrt(y)) / z
		print('Two roots: '+str(x) + ',' + str((-b - math.sqrt(y)) / z))
	# No real roots
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
