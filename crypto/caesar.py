from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    code = ""
    for char in text:
        code += rotate_character(char, rot)
    return code


def main():
    text = input("Type a phrase: ")
    rot = input("Rotate by: ")
    result = encrypt(text, rot)
    print (result)
if __name__ == '__main__':
    main()