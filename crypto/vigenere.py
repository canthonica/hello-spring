from helpers import alphabet_position, rotate_character


def encrypt(text, key):
    encrypted = []    
    start_char = 0
    for i in text:
        rot = alphabet_position(key[start_char])
        if i.isalpha():            
            encrypted.append(rotate_character(i, rot))             
            if start_char == (len(key) - 1): 
                start_char = 0
            else:
                start_char += 1   
        else:
            encrypted.append(i)

    return "".join(encrypted)


def main():
    text = input("Type a message: ")     #The crow flies at midnight! Uvs osck rmwse bh auebwsih!
    key = input("Encryption Key: ")
    result = encrypt(text, key)
    print(result)
if __name__ == '__main__':   
      main()