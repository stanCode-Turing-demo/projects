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
    for i in range(len(ans)):
        current += '-'      # initialize
    while True:
        guess = get_input(life, current)
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
    ending(life, ans)


def get_input(lives, display):
    """
    Get user input at every round
    :param lives: (int) the lives of player
    :param display: (string) the guessed answer to show user
    :return: (string) the character input from player
    """
    print('The word looks like: ' + display)
    print('You have ' + str(lives) + ' guesses left.')
    while True:
        guess_text = input('Your guess: ')
        if len(guess_text) == 1 and guess_text.isalpha():
            return guess_text.upper()
        else:
            print('Illegal format.')


def fail_guess(display):
    """
    print fail guess
    :param display: (string) the guessed character
    :return: None
    """
    print('There is no ' + display + '\'s in the word.')


def success_guess(guessed, replace, origin):
    """
    print success guess information and update the guessed correct answer
    :param guessed: the guessed correct answer
    :param replace: the just corrected character
    :param origin: the answer
    :return: the updated guessed correct answer
    """
    temp = ''
    for i in range(len(origin)):
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
        print('You win!!')
    else:
        print('You are completely hung : (')
    print('The word was: ' + display)


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
