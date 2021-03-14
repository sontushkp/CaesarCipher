def encrypt():
    print("Encryption")
    print("Message must contain either only Lower case or Upper case alphabet")
    msg = input("Enter your message: ")
    key = int(input("Enter your key(0-25): "))  # 26 letters

    encrypted_msg = ""

    for i in range(len(msg)):
        if ord(msg[i]) == 32:
            encrypted_msg += chr(ord(msg[i]))  # For space char
        elif (ord(msg[i]) + key) > 122:
            temp = (ord(msg[i]) + key) - 122
            encrypted_msg += chr(96 + temp)  # For lower case
        elif ((ord(msg[i]) + key) > 90) and ((ord(msg[i]) + key) <= 96):
            temp = (ord(msg[i]) + key) - 90
            encrypted_msg += chr(64 + temp)  # For upper case
        else:
            encrypted_msg += chr(ord(msg[i]) + key)
    print("Encrypted message: " + encrypted_msg)


def decrypt():
    print("Decryption")
    print("Message must contain either only Lower case or Upper case alphabet")
    encrypted_msg = input("Enter your encrypted message: ")
    decrypt_key = int(input("Enter your key(0-25): "))  # 26 letters

    decrypted_msg = ""

    for i in range(len(encrypted_msg)):
        if ord(encrypted_msg[i]) == 32:
            decrypted_msg += chr(ord(encrypted_msg[i]))
        elif ((ord(encrypted_msg[i]) - decrypt_key) < 97) and ((ord(encrypted_msg[i]) - decrypt_key) > 90):
            temp = (ord(encrypted_msg[i]) - decrypt_key) + 26
            decrypted_msg += chr(temp)
        elif (ord(encrypted_msg[i]) - decrypt_key) < 65:
            temp = (ord(encrypted_msg[i]) - decrypt_key) + 26
            decrypted_msg += chr(temp)
        else:
            decrypted_msg += chr((ord(encrypted_msg[i]) - decrypt_key))
    print("Decrypted Message: " + decrypted_msg)


def main():
    option = int(input("1. Encrypt\n2. Decrypt\n"))
    if option == 1:
        encrypt()
    elif option == 2:
        decrypt()
    else:
        print("Wrong Option")


if __name__ == '__main__':
    main()
