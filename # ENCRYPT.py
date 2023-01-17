# ENCRYPT
# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.isnumeric()):
            result += chr((ord(char) + s-48) % 10 + 48)

        elif(ord(char) >= 33 and ord(char) <= 47):
            result += chr((ord(char) + s - 33) % 14 + 33)
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = "angka 1"
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))
