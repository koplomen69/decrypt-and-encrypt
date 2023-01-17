# import string

Option = input('----------Selamat Datang Yahahahahay----------- \n      DECRYPT      \n Decrypt ASCII(1) \n Decrypt CESAR(2) \n ROT13        (3) \n      ENCRYPT      \n Encrypt CESAR(4) \n :')
Message = input('masukkan kode : ')
end_program = False


while not end_program:
    if Option == '1':
        decodemessage = ''
        for item in Message.split():
            decodemessage += chr(int(item))

        print(decodemessage)
        end_program = True

    elif Option == '2':
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        kecil = 'abcdefghijklmnopqrstuvwxyz'
        ongko = '0123456789'
        SIMBOL = '!"#$%&`()*+,-./'
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in Message:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                elif symbol in kecil:
                    num = kecil.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(kecil)
                    translated = translated + kecil[num]
                elif symbol in ongko:
                    num = ongko.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(ongko)
                    translated = translated + ongko[num]
                elif symbol in SIMBOL:
                    num = SIMBOL.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(SIMBOL)
                    translated = translated + SIMBOL[num]
                else:
                    translated = translated + symbol
            print('Hacking key #%s: %s' % (key, translated))
            end_program = True

    elif Option == '3':
        rot13trans = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
                                   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234')

# Function to translate plain text
        def rot13(text):
            return text.translate(rot13trans)

        def main():
            # txt = input("Masukkan Teks : ")
            print("Hasil : ", rot13(Message))

        if name == "main":
            main()
        end_program = True

    elif Option == '4':
        def encrypt(Message, s):
            result = ''

    # transverse the plain text
            for i in range(len(Message)):
                char = Message[i]

        # Encrypt uppercase characters in plain text
                if (char.isupper()):
                    result += chr((ord(char) + s - 65) % 26 + 65)
                elif (char.isnumeric()):
                    result += chr((ord(char) + s - 48) % 10 + 48)
        # Encrypt lowercase characters in plain text
                elif(ord(char) >= 33 and ord(char) <= 47):
                    result += chr((ord(char) + s - 33) % 15 + 33)
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
            return result

        # check the above function
        s = int(input("Shift Pattern : "))
        #print("Plain Text    : " + text)
        #print("Shift pattern : " + str(s))
        print("Cipher        : " + encrypt(Message, s))
        end_program = True

    else:
        print('Opsi Tidak Valdi')
        end_program = True
