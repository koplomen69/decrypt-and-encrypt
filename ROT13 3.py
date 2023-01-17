#from string import maketrans
rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                           'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234')
# Function to translate plain text


def rot13(text):
    return text.translate(rot13trans)


def main():
    txt = ('Frava,qrfrzorE')
    print('hasil rot :', rot13(txt))


if __name__ == "__main__":
    main()
