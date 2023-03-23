def encodePassword(number):
    encodedPassword = ""

    for i in range(len(number)):
        digit = int(number[i])
        digit += 3
        if digit > 10:
            digit = digit%10
        encodedPassword += f"{digit}"

    return encodedPassword

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

        elif menuOption == 2:
            print(f"The encoded password is {encodedPassword}, and the original password is {password}")
            print()

        elif menuOption == 3:
            menu = False

    quit()
if __name__ == '__main__':
    main()
