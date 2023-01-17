# Shaquille Rayhannizam/36
from logging import debug


message = ('tabaRokoraM')
translated = ''  # cipher text is stored in this variable
i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print("The cipher text is : ", translated)

