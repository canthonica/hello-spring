alphabet = "abcdefghijklmnopqrstuvwxyz"
def alphabet_position(letter):
    output = alphabet.index(letter.lower())
    return output
letter = b
print(alphabet_position(letter))

'''
def rotate_character(char, rot):
    if char.isalpha():
        new_char = alphabet_position(char)
        new_char = (new_char + rot) % (int(len(alphabet)))            
        new_char = (alphabet[new_char])
        if char.isupper():
            new_char = new_char.title()
        return new_char
    else:
        return char

    return new_char




def main():
    mess = input("Type a message: ")
    num = input("Rotate by: ")
    #result = rotate_character(x, y)  #Not needed once encrypt function works.
    result = rotate_character(mess, int(num))
    print(result)

if __name__ == "__main__":
    main()
    '''