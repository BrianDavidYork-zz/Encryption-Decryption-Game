"""Contains all the code relating to Caesar encryptions (level 1)."""
import random

# Defines the alphabet list and number list used to make the dictioniaries for encoding/decoding.
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
num = range(0, 26)

# Creates the dictionaries used to encode/decode.
alph_to_num = dict(zip(alph, num))
num_to_alph = dict(zip(num, alph))


def caesar_encode(text):
    """Randomly generates a key and returns a Caesar-encoded version of the string, based on the key."""
    key = random.randint(1, 25)
    str_key = str(key)
    text = text.lower()
    num_list = [alph_to_num[s] if s in alph else s for s in text]  # converts each letter of the text to a string
    encoded_list = [num_to_alph[(n + key) % 26] if n in num else n for n in num_list]  # adds key-value to each number
    encoded_str = ""
    for i in encoded_list:
        encoded_str += i
    print('Your key is ' + str_key)
    print('The encoded string is: ' + encoded_str)


def caesar_decode(text, key):
    """Takes an encoded string and key, and returns a Caesar-decoded string based on the key provided"""
    text = text.lower()
    num_list = [alph_to_num[s] if s in alph else s for s in text]
    decoded_list = [num_to_alph[(n - key) % 26] if n in num else n for n in num_list]
    decoded_str = ""
    for i in decoded_list:
        decoded_str += i
    print('The decoded text is ' + decoded_str)


def caesar_test():
    """randomly chooses a text from list, Caesar-encodes the text, and asks user to decode it to pass the test."""
    text_list = ['Hello World!',
                 'God Bless America',
                 'Welcome to the jungle',
                 'Meet me by the creek',
                 'Girls just want to have fun',
                 'Elephants never forget',
                 'Big red fire truck',
                 'I shot a man just to watch him die']
    ran_str = random.choice(text_list).lower()
    key = random.randint(1, 25)
    num_list = [alph_to_num[s] if s in alph else s for s in ran_str]
    encoded_list = [num_to_alph[(n + key) % 26] if n in num else n for n in num_list]
    encoded_str = ""
    for i in encoded_list:
        encoded_str += i
    print(encoded_str)
    answer = input('Can you decode this string? ')
    if answer.lower() == ran_str.lower():
        print('Congrats! You solved level 1!\n')
        pass
    elif answer != ran_str:
        print("Sorry, that's not correct.  Why don't you practice some more?\n")
        caesar()


def caesar():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit.  Type M to return to the main menu.')
        prac_test = input('would you like to practice or take the test? P/T')
        if prac_test.lower() == 'p':
            choice = input('Would you like to encode or decode? E/D ')
            if choice.lower() == 'e':
                s = input('Enter the text you would like to encode: ')
                caesar_encode(s)
            elif choice.lower() == 'd':
                s = input('Enter the text you would like to decode: ')
                k = int(input('Enter the key: '))
                caesar_decode(s, k)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif prac_test.lower() == 't':
            caesar_test()
        elif prac_test.lower() == 'q':
            exit()
        elif prac_test.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')
