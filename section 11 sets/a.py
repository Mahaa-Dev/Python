from colorama import Fore, Style


def welcome():
    print("\nWelcome to the Caesar Cipher \nThis program encrypts and decrypts text with the Caesar Cipher")


def main():

    while True:
        # Prompts user to select the mode
        mode = (input("Would you like to encrypt (e) or decrypt (d) "))
        print(Fore.RED + mode + Style.RESET_ALL)


        # Validating mode
        if mode == 'e':
            message = (input("What message would you like to encrypt: "))
            print(Fore.RED + message + Style.RESET_ALL)

        elif mode == 'd':
            message = (input("What message would you like to decrypt: "))
            print(Fore.RED + message + Style.RESET_ALL)
        else:
            print("Invalid Mode. Please Try Again!!")
            continue

        # Validating message and key (user's input) to be string and integer
        if not isinstance(message, str):
            print("Message must be string. Please try again.")
            continue

        key = int(input("Enter the key with which message should be shifted: "))
        print(Fore.RED + key + Style.RESET_ALL)

        if not isinstance(key, int):
            print("Key must be an integer. Please try again.")
            continue

            # As per requirement encrypt or decrypt function call and displays

        if mode == 'e':
            output = encrypt(message, key)
        else:
            output = decrypt(message, key)

        print(output)
        # Asks user whether they want to continue with the program or not?
        another = input("Do you want to continue: ")
        # Validate user input
        if another != 'y' and another != 'n':
            print("Invalid input. Please try again later")
            continue
        # Terminates program
        if another == 'n':
            print("Thank you!!")
            break


def encrypt(message, key):
    result = " "
# Ensure key is within the range 0-25
    key = key % 26
# Iterates over each character in the message
    for char in message:
        # Shift letter by key position
        if char.isalpha():
            char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))

            result += char
            # Add character to the result variable
        result = result.upper()

        # Returns result to the

    return result


def decrypt(encrypted_message, key):
    result = " "

    for char in encrypted_message:
        if char.isalpha():
            char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))

        result += char
        result.upper()
    return result


if __name__ == '__main__':

    welcome()
    main()
