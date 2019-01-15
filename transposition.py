import math
import random
from helper import *


def transposition_encrypt(text):
    """
    The transposition_encrypt function takes a text and rearranges the characters of the text according to a key.  If
    your text is "hello world!" and your key is three, the cipher creates three rows and rearranges the letters
    top-to-bottom and left-to-right like this:

                                                H l W l
                                                e o o d
                                                l   r !

    Then the three rows are concatenated into a single string top-to-bottom: "HlWleoodl r!"
    This is the encrypted string returned at the end of the the function.

    The "text" parameter should be a string.
    """
    text = text
    key = random.randint(2, (len(text) // 2))  # randomly generates key between two and half the length of the text.

    cipher_text = [''] * key  # creates as may rows as the key value.

    # rearranges the text top-to-bottom and left-to-right
    for column in range(key):
        current_index = column

        while current_index < len(text):
            cipher_text[column] += text[current_index]
            current_index += key

    encrypted_message = ''.join(cipher_text)

    return encrypted_message


def transposition_decrypt(text, key):
    """
    The transposition_decrypt function takes a text and a key.  The number of rows is equal to the key, and the number
    of columns is determined by the length of the text and the key.  Then the text is rearranged/deciphered so that
    it can be read in ordinary english.

    For example, if your encrypted message is "HlWleoodl r!" and your key is three, you would have three rows in which
    to rearrange your letters:

                                H l W l
                                e o o d
                                l   r !

    The message is then concatenated top-to-bottom and left-to-right to return the decrypred message: "Hello World!"

    The "text" parameter should be a string.
    The "key" parameter should be an integer.

    The transposition_decrypt function is kept separate from the transposition_encrypt function, because they use
    different code with almost no repetition.  Combining them is unnecessary.
    """
    # Determines the number of columns by taking the length of thte text and dividing by the key.
    num_columns = int(math.ceil(len(text) / float(key)))
    num_rows = key
    # Determines the number of unused spaces at the bottom of the last column.
    empty_squares = (num_columns * num_rows) - len(text)

    deciphered_text = [''] * num_columns

    column = 0
    row = 0

    # rearranges the encrypted text using the correct number of columns and rows.
    for symbol in text:
        deciphered_text[column] += symbol
        column += 1

        if (column == num_columns) or (column == num_columns - 1 and row >= num_rows - empty_squares):
            column = 0
            row += 1

    return ''.join(deciphered_text)


def transposition_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit.  Type M to return to the main menu.')
        prac_test = input('would you like to practice or take the test? P/T ')
        if prac_test.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = transposition_encrypt(text)
                print('Your encrypted text is ' + message)
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                key = int(input('Enter the key: '))
                message = transposition_decrypt(text, key)
                print('Your decrypted text is ' + message)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif prac_test.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = transposition_encrypt(text)
            print(encrypted_text)
            answer = input('s/nCan you decode this string? ')
            if answer.lower() == text.lower():
                print('Congrats! You solved level 4!\n')
                break
            elif answer.lower() != text.lower():
                print("Sorry, that's not correct.  Why don't you practice some more?\n")
                transposition_main()
        elif prac_test.lower() == 'q':
            exit()
        elif prac_test.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')

