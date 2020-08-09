"""
File: complement.py
Name: Max Chang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO: Give a DNA strand and print the complement DNA sequence
    """
    dna = input('Please Give me a DNA strand and I\'ll find the complement:')
    new_dna = complement(dna.upper())
    print('The complement of ' + dna + ' is ' + new_dna)


def complement(dna):
    """
    This function will return the complement of dna sequence of the input sequence
    :param dna: (string) original dna
    :return: (string) complement dna
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        if base == 'T':
            ans += 'A'
        if base == 'C':
            ans += 'G'
        if base == 'G':
            ans += 'C'
    return ans



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
