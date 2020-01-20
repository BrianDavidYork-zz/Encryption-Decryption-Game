from caesar import *
from vigenere import *
from reverse import *
from transposition import *

def main():
    """Main program.

    Explains the rules, asks user which difficulty level they would like to try.  Based on user answer
    one of the three encryption/decryption programs is launched.
    """
    print("Hello and welcome to my encryption game\n"
          "There are four difficulty levels, each using a different method of encryption.\n"
          "Within each level, you can practice encoding and decoding, until you have mastered the encryption method.\n"
          "After that, you can take a test to prove that you are a master cryptographer!\n")

    while True:
        level = str(input("Enter 1, 2, 3, or 4 to select a difficulty level, or enter Q to quit. "))
        if level == '1':
            reverse_main()
        elif level == '2':
            caesar_main()
        elif level == '3':
            vigenere_main()
        elif level == '4':
            transposition_main()
        elif level.lower() == 'q':
            exit()
        else:
            pass


main()
