def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = alphabet.index(letter.lower())
    return output

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        new_char = alphabet_position(char)
        new_char = (new_char + int(rot)) % 26           
        new_char = (alphabet[new_char])
        if char.isupper():
            new_char = new_char.title()
        return new_char
    else:
        return char