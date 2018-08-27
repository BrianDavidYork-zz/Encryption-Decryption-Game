import caesar
import vigenere


def main():
    """Main program.

    Explains the rules, asks user which difficulty level they would like to try.  Based on user answer
    one of the three encryption/decryption programs is launched.
    """
    print("Hello and welcome to my encoder/decoder program!\n"
          "There are three difficulty levels, each using a different method of encryption.\n"
          "Within each level, you can practice encoding and decoding, until you have mastered the encryption method.\n"
          "After that, you can take a test to prove that you are a master cryptographer!\n")

    while True:
        level = input("Enter 1 or 2 to select a difficulty level, or enter Q to quit.")
        if level == '1':
            caesar.caesar()
        elif level == '2':
            vigenere.vigenere()
        elif level.lower() == 'q':
            exit()
        else:
            print('please enter 1, 2, or 3 to choose your difficulty level.')


main()
