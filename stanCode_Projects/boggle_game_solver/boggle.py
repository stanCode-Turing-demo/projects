"""
File: boggle.py
Name: Josephine
----------------------------------------
This program can find all words in a 4x4 square grid which input by the user.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global Variables
dictionary = []  # This is a list of dictionary.
searching_list = []  # This is a list of searching results.


def main():
	"""
	This program can record 16 letters which input by the user into an array.
	Then use the 'find_anagrams' function to find every single word in the array, print them,
	and add them into 'searching_list'.
	Finally, print the amount of words in 'searching_list'.
	"""
	read_dictionary()
	row_all = []  # A list which records row1 - row4 (the user input).
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		# This condition will make sure that the user type in the right style.
		if len(row) > 7 or len(row) < 7 or row[1] and row[3] and row[5] is not ' ':
			print('Illegal input')
			return
		row = row.split(' ')
		row_all.append(row)
	check_alpha = []  # A list of four [0, 0, 0, 0].
	# Using 2 for loop to pick each letter in 'row_all'.
	for j in range(4):
		for k in range(4):
			for x in range(4):
				check_alpha.append([0, 0, 0, 0])
			check_alpha[j][k] = 1
			find_anagrams(row_all, check_alpha, current_list=[row_all[j][k]], current_row=j, current_alpha=k)
			check_alpha = []
	# Print the final result.
	print(f'There are {len(searching_list)} words in total.')


def find_anagrams(row_all, check_alpha, current_list, current_row, current_alpha):
	"""
	This function use recursion to find all the possible permutations of letters in 'row_all'.
	:param row_all: list, a list contains the user input
	:param check_alpha: list, a list of four [0, 0, 0, 0]
	:param current_list: list, an empty list
	:param current_row: int, a row of the starting letter (the number of the row)
	:param current_alpha: int, a sequence of the staring letter (the number of the alpha in a row)
	:return: nothing / this function only adds words into the global variable'searching_list'
	"""
	global searching_list
	if has_prefix(current_list):
		# Using 2 for loop to pick each letter around the current letter.
		for r in range(-1, 2):
			for a in range(-1, 2):
				# This condition will make sure the picked-letter will not out of scope.
				if 0 <= current_row + r < 4 and 0 <= current_alpha + a < 4:
					new_current_row = current_row + r
					new_current_alpha = current_alpha + a
					# This condition will check out if the picked-letter is already in the current_list.
					if check_alpha[new_current_row][new_current_alpha] != 1:
						current_list.append(row_all[new_current_row][new_current_alpha])
						check_alpha[new_current_row][new_current_alpha] = 1
						# Turns the list into string, and check if the string is in the dictionary.
						if len(current_list) >= 4:
							current_str = ''
							for ch in current_list:
								current_str += ch
							if current_str in dictionary:
								if current_str not in searching_list:
									searching_list += [current_str]
									print(f'Found \"{current_str}\"')
						# Recursion
						find_anagrams(row_all, check_alpha, current_list, new_current_row, new_current_alpha)
						current_list.pop()
						check_alpha[new_current_row][new_current_alpha] = 0
				else:
					pass


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, 'r') as file:
		for line in file:
			dictionary += [line.strip()]


def has_prefix(current_list):
	"""
	This function can make sure that the current string is in the dictionary.
	(or it will return False and stop finding.
	:param current_list: (list) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in current_list
	"""
	current_str = ''
	for ch in current_list:
		current_str += ch
	for word in dictionary:
		if word.startswith(current_str):
			return True
	return False


if __name__ == '__main__':
	main()
