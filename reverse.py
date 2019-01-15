import random
from helper import *


def reverse(text):

    """
    The reverse cipher reverses the order of a string.

    For example, if the text is 'Hello World!', the reversed text would be '!dlroW olleH'

    The "text" parameter should be a string.
    """
    text = text
    reverse_str = text[::-1]
    return reverse_str


def reverse_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit.  Type M to return to the main menu.')
        prac_test = input('would you like to practice or take the test? P/T ')
        if prac_test.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = reverse(text)
                print('Your encrypted text is ' + message)
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                message = reverse(text)
                print('Your decrypted text is ' + message)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif prac_test.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = reverse(text)
            print(encrypted_text)
            answer = input('s/nCan you decode this string? ')
            if answer.lower() == text.lower():
                print('Congrats! You solved level 1!\n')
                break
            elif answer.lower() != text.lower():
                print("Sorry, that's not correct.  Why don't you practice some more?\n")
                reverse_main()
        elif prac_test.lower() == 'q':
            exit()
        elif prac_test.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')
