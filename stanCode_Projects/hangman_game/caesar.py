"""
File: caesar.py
Name: Max Chang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: Decipher the code using Caesar Cipher
    """
    secret = secret_input('Secret Number: ')
    cipher_text = input('What\'s the ciphered string? ')
    print('The deciphered string is: ' + decipher(cipher_text.upper(), secret))


def secret_input(display):
    """
    Get the shift index for Caesar Cipher
    :param display: (string) text to show in the console
    :return: (int) the Caesar Cipher shift index
    """
    while True:
        secret = input(display)
        if secret.isdigit() or (secret[0] == '-' and secret[1:].isdigit()):
            secret = int(secret)
            while True:
                if 0 <= secret < len(ALPHABET):
                    return secret
                elif secret < 0:    # Handle for minus
                    secret += len(ALPHABET)
                else:               # Handle for larger than 26
                    secret -= len(ALPHABET)
        print('Not an integer number')


def decipher(cipher, key):
    """
    Decipher the encrypted code from user using key
    :param cipher: (string) the encrypted code
    :param key: (int) Caesar Cipher key
    :return: (string) deciphered string
    """
    decipher_text = ''
    for i in range(len(cipher)):
        if cipher[i].isalpha():
            position = ALPHABET.find(cipher[i])
            if position + key < len(ALPHABET):
                decipher_text += ALPHABET[position + key]
            else:       # Handle for index larger than 26
                decipher_text += ALPHABET[position + key - len(ALPHABET)]
        else:           # Handle for non-alphabet
            decipher_text += cipher[i]
    return decipher_text


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
