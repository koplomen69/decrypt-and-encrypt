ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def read_json(filename):
    with open(cwd+'/'+filename+'.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(data, filename):
    with open(cwd+'/'+filename+'.json', 'w') as file:
        json.dump(data, file, indent=4)


def Encode(message, shift):
    """
    Encodes a message into a caesar cipher

    Params:
     - message (str) : Message to encode
     - shift (int) : Shift

    Returns:
     - encodedMessage (str) : The encoded message
    """
    shift += 1
    encodedMessage = ''
    message = message.lower()  # Work with everything lowercase, its easier

    for letterIndex in range(len(message)):
        # Handle spaces
        if message[letterIndex] in [' ', '!', '?', '.', '-', ',', '_']:
            encodedMessage += message[letterIndex]
        else:
            try:
                index = ALPHABET.index(message[letterIndex]) + shift

                # If our index after shifting is bigger then ALPHABET handle it
                while index > len(ALPHABET):
                    index -= len(ALPHABET)

                # Now its just string substitution
                encodedMessage += ALPHABET[index-1]
            except Exception as e:
                print("A problem occured:", e)
                encodedMessage += '?'

    return encodedMessage


def Decode(message, shift=-1):
    """
    Decodes a message from a caesar cipher

    Params:
     - message (str) : Message to decode
    Optional Params:
     - shift (int) : If shift is known

    Returns:
     - decodedMessage (str) : The decoded message
    """
    decodedMessage = ''
    message = message.lower()  # lowercase is easier to work with

    # If the shift is known it is simple to decode
    if shift != -1:
        for letterIndex in range(len(message)):
            if message[letterIndex] in [' ', '!', '?', '.', '-', ',', '_']:
                decodedMessage += message[letterIndex]
            else:
                try:
                    index = ALPHABET.index(message[letterIndex]) - shift

                    # If the index is smaller then ALPHABET, handle it
                    while index < 0:
                        index += len(ALPHABET)

                    decodedMessage += ALPHABET[index]
                except Exception as e:
                    print("A problem occured:", e)
                    decodedMessage += '?'

        return decodedMessage
    else:  # If shift is not known, figure it out thru brute force
        data = read_json('words_dictionary')
        for i in range(len(ALPHABET)):
            decodedMessage = Decode(message, i+1)
            wordList = decodedMessage.split(" ")
            try:
                # Loop over words counting english words
                count = 0
                for word in wordList:
                    if word in data.keys():
                        count += 1

                    # More accurate this way compared to only one word checks
                    if count > len(wordList) / 2:
                        return decodedMessage
            except KeyError:
                continue


encoded = Encode("Github: Skelmis", 6)
print(encoded)
#encoded = Encode("Hello world", 5)
# print(encoded)
decoded = Decode(
    "Kszqcas hc hvwg qcadshwhwcb! Vsfs wg hvs hslh hc hvs twfgh vozt ct hvs qvozzsbus cgbyly")
print(decoded)
