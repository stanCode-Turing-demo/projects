"""
File: anagram.py
Name: Josephine
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 21

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'       # Controls when to stop the loop

# Global Variables
dictionary = []  # This is a list of dictionary.
searching_list = []  # This is a list of searching results.


def main():
    """
    This program use the 'find_anagrams' function to find all the anagram(s) for the word input by user.
    Then, it will print all the results and the total amount of the results.
    """
    global searching_list
    read_dictionary()
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    word = input('Find anagrams for: ')
    # Before user typing the EXIT number, this program will keep working.
    while word != '-1':
        current_str = []
        print('Searching...')
        find_anagrams(word, current_str)
        print(f'{len(searching_list)} anagrams: {searching_list}')
        # Clear the list 'searching_list' and then restart.
        searching_list = []
        word = input('Find anagrams for: ')
    return


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list.
    """
    global dictionary
    with open(FILE, 'r') as file:
        for line in file:
            dictionary += [line.strip()]


def find_anagrams(s, current_index):
    """
    This function use recursion to find all the possible permutations of s (the user input).
    :param s: string, the user input word
    :param current_index: list, a empty list which will be use to record the index
    :return: nothing / this function only adds words into the global variable'searching_list'
    """
    global searching_list
    # Base-Case
    if len(current_index) == len(s):
        current_str = ''
        # Turns the index list into string, and check if the string is in the dictionary.
        for digit in current_index:
            current_str += s[digit]
        if current_str in dictionary:
            if current_str not in searching_list:
                searching_list += [current_str]
                print('Found: ' + current_str)
                print('Searching...')
    else:
        if has_prefix(s, current_index):
            for i in range(len(s)):
                if i in current_index:
                    pass
                else:
                    current_index.append(i)
                    # Recursion
                    find_anagrams(s, current_index)
                    current_index.pop()
        else:
            return


def has_prefix(s, sub_index):
    """
    This function can make sure that the current string(recorded in index) is in the dictionary.
    (or it will return False and stop finding.
    :param s: string, the user input word
    :param sub_index: list, current list (recorded in the index type)
    :return: (bool) If there is any words with prefix stored in current list(recorded in index)
    """
    current_str = ''
    for digit in sub_index:
        current_str += s[digit]
    for word in dictionary:
        if word.startswith(current_str):
            return True
    return False




if __name__ == '__main__':
    main()
