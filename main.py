#this is Ryan Rues's main.py file

def encode(password):
    encodedDigits = [str(int(digit) + 3) for digit in password if digit.isdigit()]
    encodedPassword = ''.join(encodedDigits)
    return encodedPassword

def print_menu():
    print("Menu \n------------- \n1. Encode \n2. Decode\n3. Quit")
    selection = int(input("Please enter an option: "))
    return selection

def decode(password):
    decodedDigits = [str(int(digit) - 3) for digit in password if digit.isdigit()]
    decodedPassword = ''.join(decodedDigits)
    return decodedPassword

def main():
    while True:
        selection = print_menu()
        if selection == 1:
            password = str(input("Please enter your password: "))
            encodedPass = encode(password)
            print("Your password has been encoded and stored!")
        elif selection == 2:
            decodedPass = decode(encodedPass)
            print("The encoded password is " + encodedPass +
                  ", and the origonal password is " + decodedPass + ".")
        elif selection == 3:
            break
        else:
            print("Invalid selection")



if __name__ == "__main__":
    main()