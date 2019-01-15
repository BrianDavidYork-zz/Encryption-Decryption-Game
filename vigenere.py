import random
import itertools
from helper import *


def vigenere(mode, text, key=None):
    """
    The Vigenere function takes a text and either encrypts or decrypts it according to the key word provided.  The
    function works like the Caesar function, except instead of changing every letter of the text by the same increment,
    it uses a key-word changed into a series of numbers that is then applied to the text.

    For example, if you are encrypting the text 'abc', and your key is 'bad', the encrypted string would be 'bbf'
    because a = 0, b = 1, c = 2, d = 3 ... and the key of 'bad' adds the series of numbers (1, 0, 3) to  to the text
    translated into numbers (0, 1, 2), which adds up to (1, 1, 5) or 'bbf'.

    The function takes 3 parameters:
        1) "mode" tells the function to encrypt (add the key value) or decrypt (subtract the key value)
        2) "text" is the string to be encrypted or decrypted
        3) "key" is the string that will be used to decrypt your message.  If you are encrypting, the key is random.

    The dictionaries that convert between letters and numbers are stored in the .helper file, imported above.
    """
    mode = mode
    text = text.lower()
    if mode == 'encrypt':
        key = random.choice(cipher_key)
    elif mode == 'decrypt':
        key = key
    k = itertools.cycle(key)  # creates an infinite iteration over the key
    key_list = []
    new_list = []
    # creates a list as long as the text from the variable k
    i = 1
    while i <= len(text):
        key_list.append(next(k))
        i += 1
    # converts each letter of the text to a number
    num_list = [alph_to_num[s] if s in alph else s for s in text]
    # converts each letter of the string in the variable key_list to a number
    num_key_list = [alph_to_num[s] for s in key_list]
    for num1, num2 in zip(num_list, num_key_list):
        if num1 in num:
            if mode == 'encrypt':
                # adds the numeric values of the text and key together
                new_list.append(num1 + num2)
            elif mode == 'decrypt':
                # subtracts the numeric values of the text and key together
                new_list.append(num1 - num2)
        else:
            new_list.append(num1)
    decoded_list = [num_to_alph[n % 26] if isinstance(n, int) else n for n in new_list]
    new_str = ""
    for i in decoded_list:
        new_str += i
    return new_str


def vigenere_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit.  Type M to return to the main menu.')
        prac_test = input('would you like to practice or take the test? P/T ')
        if prac_test.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = vigenere('encrypt', text)
                print('Your encrypted text is ' + message)
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                key = input('Enter the key: ')
                message = vigenere('decrypt', text, key)
                print('Your decrypted text is ' + message)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif prac_test.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = vigenere('encrypt', text)
            print(encrypted_text)
            answer = input('s/nCan you decode this string? ')
            if answer.lower() == text.lower():
                print('Congrats! You solved level 3!\n')
                break
            elif answer.lower() != text.lower():
                print("Sorry, that's not correct.  Why don't you practice some more?\n")
                vigenere_main()
        elif prac_test.lower() == 'q':
            exit()
        elif prac_test.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')
