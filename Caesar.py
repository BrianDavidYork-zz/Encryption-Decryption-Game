import random
from helper import *


def caesar(mode, text, key=None):
    """
    The Caesar Cipher takes a string, and, for each letter in the string, converts the letter to a different one.
    It does this by associating each letter with a number, and uses the key to get a new numeric value that is then
    translated back into a new encrypted string.

    For example, if you are encrypting the text 'abc', and your key is 1, the encrypted string would be 'bcd' because
    a = 0, b = 1, c = 2, d = 3 ... and the key of 1 adds 1 to the number corresponding number of each letter in the
    text.

    The function takes 3 parameters:
        1) "mode" tells the function to encrypt (add the key value) or decrypt (subtract the key value)
        2) "text" is the text to be encrypted or decrypted
        3) "key" is the numeric key that will be used to decrypt your message.  If you are encrypting, the key is
            random.

    The dictionaries that convert between letters and numbers are stored in the .helper file, imported above.
    """
    mode = mode
    if mode == 'encrypt':
        key = random.randint(1, 25)
    elif mode == 'decrypt':
        key = key
    str_key = str(key)
    text = text.lower()
    # converts each letter of the text to a number
    num_list = [alph_to_num[s] if s in alph else s for s in text]
    if mode == 'encrypt':
        # adds key-value to each number
        new_list = [num_to_alph[(n + key) % 26] if n in num else n for n in num_list]
    elif mode == 'decrypt':
        # subtracts key-value from each number
        new_list = [num_to_alph[(n - key) % 26] if n in num else n for n in num_list]
    new_str = ''
    for i in new_list:
        new_str += i
    return new_str, str_key


def caesar_main():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit.  Type M to return to the main menu.')
        prac_test = input('would you like to practice or take the test? P/T ')
        if prac_test.lower() == 'p':
            choice = input('Would you like to encrypt or decrypt? E/D ')
            if choice.lower() == 'e':
                text = input('Enter the text you would like to encode: ')
                message = caesar('encrypt', text)
                print('Your encrypted text is ' + message[0])
            elif choice.lower() == 'd':
                text = input('Enter the text you would like to decode: ')
                key = int(input('Enter the key: '))
                message = caesar('decrypt', text, key)
                print('Your decrypted text is ' + message[0])
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif prac_test.lower() == 't':
            text = random.choice(text_list)
            encrypted_text = caesar('encrypt', text)
            print(encrypted_text[0])
            answer = input('s/nCan you decode this string? ')
            if answer.lower() == text.lower():
                print('Congrats! You solved level 2!\n')
                break
            elif answer.lower() != text.lower():
                print("Sorry, that's not correct.  Why don't you practice some more?\n")
                caesar_main()
        elif prac_test.lower() == 'q':
            exit()
        elif prac_test.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')
