"""
File: hangman.py
Name: Max Chang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    TODO: Play a hangman game
    """
    ans = random_word()
    life = N_TURNS
    current = ''        # text to display guessed answer
    guessed = ''        # text to store guessed character
    for i in range(len(ans)):
        current += '-'      # initialize display string
    while True:
        guess = get_input(life, current, guessed)
        if guess not in guessed:
            guessed += guess + ', '
        location = ans.find(guess)
        if location == -1:          # fail guess
            life -= 1
            fail_guess(guess)
            if life == 0:           # dead
                break
        else:                       # success guess
            current = success_guess(current, guess, ans)
            if current == ans:      # win
                break
        console_hangman(life)
    ending(life, ans)


def get_input(lives, display, guessed_text):
    """
    Get user input at every round
    :param lives: (int) the lives of player
    :param display: (string) the guessed answer to show user
    :param guessed_text: (string) the guessed character
    :return: (string) the character input from player
    """
    print('The word looks like: ' + display)
    print('You have ' + str(lives) + ' guesses left.')
    print('You have guessed: ' + guessed_text)
    while True:
        guess_text = input('Your guess: ')
        if len(guess_text) == 1 and guess_text.isalpha():
            return guess_text.upper()
        else:
            print('Illegal format.')


def fail_guess(display):
    """
    print fail guess message
    :param display: (string) the guessed character
    :return: None
    """
    print('There is no ' + display + '\'s in the word.')


def success_guess(guessed, replace, origin):
    """
    print success guess message and update the guessed correct answer
    :param guessed: the guessed correct answer
    :param replace: the just corrected character
    :param origin: the answer
    :return: the updated guessed correct answer
    """
    temp = ''
    for i in range(len(origin)):        # update display string
        if origin[i] == replace:
            temp += replace
        else:
            temp += guessed[i]
    print('You are correct!')
    return temp


def ending(lives, display):
    """
    The ending of the game
    :param lives: (int) the remaining of lives
    :param display: (string) the answer
    :return: none
    """
    if not lives == 0:
        print('')
        print('You win!!')
        print('')
        print('-----')
        print('| Thank you!!')
        print('|   O')
        print('| \\ | /')
        print('|  / \\')
    else:
        print('You are completely hung : (')
        console_hangman(lives)
    print('')
    print('The word was: ' + display)


def console_hangman(lives):
    """
    Print the hangman in console
    :param lives: (int) lives remain
    :return: None
    """
    if lives == 7:
        print('-----')
        print('|')
        print('|')
        print('|')
        print('|')
    elif lives == 6:
        print('-----')
        print('|   |')
        print('|')
        print('|')
        print('|')
    elif lives == 5:
        print('-----')
        print('|   |')
        print('|   O')
        print('|')
        print('|')
    elif lives == 4:
        print('-----')
        print('|   |')
        print('|   O')
        print('|   |')
        print('|')
    elif lives == 3:
        print('-----')
        print('|   |')
        print('|   O')
        print('| / |')
        print('|')
    elif lives == 2:
        print('-----')
        print('|   |')
        print('|   O')
        print('| / | \\')
        print('|')
    elif lives == 1:
        print('-----')
        print('|   |')
        print('|   O')
        print('| / | \\')
        print('|  /')
    else:
        print('-----')
        print('|   |')
        print('|   O')
        print('| / | \\')
        print('|  / \\')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
