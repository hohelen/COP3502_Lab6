"""
Lab 6: Software Engineering
Coder: Helen Ho
Description: Design a simple encoder/decoder program in this lab. The program will provide a looping
menu that invites the user to choose from a menu with encoder and decoder options.
"""

# Each digit of the 8-digit password is shifted up by 3 numbers
def encodePassword(number):
    encodedPassword = ""

    for i in range(len(number)):
        digit = int(number[i])
        digit += 3
        if digit > 10:
            digit = digit%10
        encodedPassword += f"{digit}"

    return encodedPassword

# Shows the menu options for the user
def displayMenu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def main():
    menu = True
    while menu:
        displayMenu()
        menuOption = int(input("Please enter an option: "))

        if menuOption == 1:
            password = input("Please enter your password to encode: ")
            encodedPassword = encodePassword(password)
            print("Your password has been encoded and stored!")
            print()

        # The password decoder takes in the encoded password and returns the original password
        elif menuOption == 2:
            print(f"The encoded password is {encodedPassword}, and the original password is {password}")
            print()

        elif menuOption == 3:
            menu = False

    quit()
if __name__ == '__main__':
    main()
