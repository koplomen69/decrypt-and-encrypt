message = ("Xnzvf'abirzorET")  # encrypted message

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 'abcdefghijklmnopqrstuvwxyz'
angka = '1234567890'
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        elif symbol in a:
            num = a.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(a)
            translated = translated + a[num]
        elif symbol in angka:
            num = angka.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(angka)
            translated = translated + angka[num]
        else:
            translated = translated + symbol

    print('Hacking key #%s: %s' % (key, translated))
