"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program present the process of Hailstone sequence.
    Users allowed to input a integer n, n > 0.
    At the end, it will always stop with 1, and showing how many steps it went through.
    """
    print('This program computes Hailstone sequence.')
    n = int(input('Enter a number: '))
    times = 0

    if n == 1:
        print('It took ' + str(times) + ' step to reach 1.')
        
    else:
        while True:
            if n % 2 == 1:
                outcome = 3 * n + 1
                print(str(int(n)) + ' is odd, ' + 'so I make 3n+1: ' + str(int(outcome)))
                n = outcome
                times = counting_steps(times)
                if outcome == 1:
                    break
            else:
                outcome = n / 2
                print(str(int(n)) + ' is even, ' + 'so I take half: ' + str(int(outcome)))
                n = outcome
                times = counting_steps(times)
                if outcome == 1:
                    break
        print('It took ' + str(times) + ' steps to reach 1.')


def counting_steps(t):
    """
    :param t: int, starts from 0.
    :return: int, return times + 1.
    """
    t += 1
    return t


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
