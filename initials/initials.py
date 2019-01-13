def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    name = fullname.title()
    name_splice = name.split()
    initials = ""
    for char in name_splice:
        initials += char[0].upper()
    
    return initials        
    
def main():
    fullname = (input("What is your full name"))
    print("Your initials are", get_initials(fullname))
          
if __name__ == "__main__":
    main()
