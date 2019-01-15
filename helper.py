# Defines the alphabet list and number list used to make the dictionaries in the caesar and vigenere functions.
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']

num = range(0, 26)

# Creates the dictionaries used in the caesar and vigenere functions.
alph_to_num = dict(zip(alph, num))
num_to_alph = dict(zip(num, alph))

# texts to be encrypted
text_list = ['Hello World!',
             'God Bless America',
             'Welcome to the jungle',
             'Meet me by the creek',
             'Girls just want to have fun',
             'Elephants never forget',
             'Big red fire truck',
             'I shot a man just to watch him die',
             'Help me please!',
             'Over my dead body',
             'Down south in Dixie',
             'Over the hills and far away'
             ]

# keys for vigenere cipher
cipher_key = [
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
            'melon',
            'red',
            'blue',
            'green',
            'yellow',
            'orange',
            'violet',
            'purple',
            'white',
            'black'
            ]

