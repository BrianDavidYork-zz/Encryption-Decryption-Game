"""Contains all the code relating to Vigenere encryptions (level 2)."""
import random
import itertools

# Defines the alphabet list and number list used to make the dictionaries for encoding/decoding.
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
num = range(0, 26)

# Creates the dictionaries used to encode/decode.
alph_to_num = dict(zip(alph, num))
num_to_alph = dict(zip(num, alph))


def vigenere_encode(text):
    """Randomly generates a key and returns a Vigenere-encoded version of the string, based on the key."""
    text = text.lower()
    key = random.choice([
            'lemon',
            'apple',
            'pear',
            'banana',
            'peach',
            'strawberry',
            'goji',
            'kiwi',
            'lime',
            'tomato',
            'melon'])
    k = itertools.cycle(key)
    key_list = []
    encoded_list = []
    i = 1
    while i <= len(text):
        key_list.append(next(k))
        i += 1
    num_list = [alph_to_num[s] if s in alph else s for s in text]
    num_key_list = [alph_to_num[s] if s in alph else s for s in key_list]
    for num1, num2 in zip(num_list, num_key_list):
        if num1 in num:
            encoded_list.append(num1 + num2)
        else:
            encoded_list.append(num1)
    encoded_list = [num_to_alph[n % 26] if isinstance(n, int) else n for n in encoded_list]
    encoded_str = ""
    for i in encoded_list:
        encoded_str += i
    print('Your key is: ' + key)
    print('The encoded string is: ' + encoded_str)


def vigenere_decode(text, key):
    """Takes an encoded string and key, and returns a Vigenere-decoded string based on the key provided"""
    text = text.lower()
    k = itertools.cycle(key)
    key_list = []
    decoded_list = []
    i = 1
    while i <= len(text):
        key_list.append(next(k))
        i += 1
    num_list = [alph_to_num[s] if s in alph else s for s in text]
    num_key_list = [alph_to_num[s] for s in key_list]
    for num1, num2 in zip(num_list, num_key_list):
        if num1 in num:
            decoded_list.append(num1 - num2)
        else:
            decoded_list.append(num1)
    decoded_list = [num_to_alph[n % 26] if isinstance(n, int) else n for n in decoded_list]
    decoded_str = ""
    for i in decoded_list:
        decoded_str += i
    print('Your decoded text is: ' + decoded_str)


def vigenere_test():
    """randomly chooses a text from list, Vigenere-encodes the text, and asks user to decode it to pass the test."""
    text_list = [
                 'Hello World!',
                 'God Bless America',
                 'Welcome to the jungle',
                 'Meet me by the creek',
                 'Girls just want to have fun',
                 'Elephants never forget',
                 'Big red fire truck',
                 'I shot a man just to watch him die']
    ran_str = random.choice(text_list).lower()
    key = random.choice([
                'red',
                'blue',
                'green',
                'yellow',
                'orange',
                'violet',
                'purple',
                'white',
                'black'])
    k = itertools.cycle(key)
    key_list = []
    encoded_list = []
    i = 1
    while i <= len(text):
        key_list.append(next(k))
        i += 1
    num_list = [alph_to_num[s] if s in alph else s for s in ran_str]
    num_key_list = [alph_to_num[s] if s in alph else s for s in key_list]
    for num1, num2 in zip(num_list, num_key_list):
        if num1 in num:
            encoded_list.append(num1 + num2)
        else:
            encoded_list.append(num1)
    encoded_list = [num_to_alph[n % 26] if isinstance(n, int) else n for n in encoded_list]
    encoded_str = ""
    for i in encoded_list:
        encoded_str += i
    print(encoded_str)
    answer = input('Can you decode this string?\n '
                   'Hint: the key is ' + str(len(key)) + ' letters long.')
    if answer.lower() == ran_str.lower():
        print('Congrats! You solved level 2!\n')
        pass
    elif answer != ran_str:
        print("Sorry, that's not correct.  Why don't you practice some more?\n")
        vigenere()


def vigenere():
    """Asks user if they want to practice (encode or decode) or take the test, and calls the corresponding function."""
    while True:
        print('Type Q to quit.  Type M to return to the main menu.')
        prac_test = input('would you like to practice or take the test? P/T')
        if prac_test.lower() == 'p':
            choice = input('Would you like to encode or decode? E/D ')
            if choice.lower() == 'e':
                s = input('Enter the text you would like to encode: ')
                vigenere_encode(s)
            elif choice.lower() == 'd':
                s = input('Enter the text you would like to decode: ')
                k = input('Enter the key: ')
                vigenere_decode(s, k)
            else:
                print('You must enter either "E" or "D" to encode or decode a text. ')
        elif prac_test.lower() == 't':
            vigenere_test()
        elif prac_test.lower() == 'q':
            exit()
        elif prac_test.lower() == 'm':
            break
        else:
            print('Please enter a valid choice.')
