# Shaquille Rayhannizam
# ENCRYPT
def encrypt(text, s):
    result = " "

    # transverse the plain text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        elif (char.isnumeric()):
            result += chr((ord(char) + s-48) % 10 + 48)

        elif (ord(char) >= 33 and ord(char) <= 47):
            result += chr((ord(char) + s - 33) % 15 + 33)

        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = ("ksajhd")
s = -13
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher: " + encrypt(text, s))
