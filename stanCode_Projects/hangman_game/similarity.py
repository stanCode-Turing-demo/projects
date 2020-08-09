"""
File: similarity.py
Name: Max Chang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO: Print the most similarity sequence input with target sequence
    """
    input_dna = input('Please give me a DNA sequence to search: ')
    target_dna = input('What DNA sequence would you like to match? ')
    print('The best match is ' + similarity(input_dna.upper(), target_dna.upper()))


def similarity(origin, target):
    """
    This function will return the string of the best match of the DNA sequence
    :param origin: The original DNA sequence
    :param target: The DNA sequence to match
    :return: The best match sequence
    """
    mostsim = 0                          # initial of the most similarity index
    if len(origin) < len(target):        # return origin if target is longer than origin
        return origin
    for i in range(len(origin) - len(target) + 1):
        sim = 0                          # initial of similarity index
        if not i:                        # First Round
            for j in range(len(target)):
                if origin[j] == target[j]:
                    sim += 1
            if sim == len(target):          # return if totally match
                return target
            mostsim = sim                   # Store the most similarity index and sequence when first round
            most = origin[:len(target)]
        else:
            for j in range(len(target)):
                if origin[i + j] == target[j]:
                    sim += 1
            if sim == len(target):                  # return if totally match
                return target
            elif mostsim < sim:
                mostsim = sim                       # Replace the most similarity index and sequence
                most = origin[i:i + len(target)]
    return most


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
