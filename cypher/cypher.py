# This is the first project from freeCodeCamp's Scientific Computing with Python (currently in Beta),
# available at https://www.freecodecamp.org/learn/scientific-computing-with-python.
#
# This is by no means a fully fledged cypher program, more of an exploration of Python, since I am dabbling
# in it for the first time (c++ is more structured, but I appreciate some quality of life decisions they took
# when developing Python)

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if not char.isalpha():
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

def main():
    print('Hello, welcome to a simple cypher project from freeCodeCamp.org')
    cypher_type = str.lower(input('Please which type of "encryption" you want to use, (C)aesar or (V)igenère cyphers? (c/v)\n'))
    match cypher_type:
        case 'c':
            print('You chose to use the Caesar cypher')
            text = input('What is the text you want to encrypt? (default = Hello World)\n')
            shift = input('What is the offset you want to use? (default = 3)\n')
            while not shift.isdecimal():
                if not shift:
                    shift = '3'
                    continue
                shift = input('What is the offset you want to use? (default = 3)\n')

            if not text:
                text = 'Hello World'
            print(f'Original text: {text} -> Caesar\'s cypher: {caesar(text, int(shift))}')

        case 'v':
            print('You chose to use the vigenère cypher')
            operation = 'decrypt' if input('What operation you want to do? (e)ncrypt or (d)ecrypt (default = encrypt)\n') == 'd' else 'encrypt'
            # Set defaults based on operation
            default_text= "mrttaqrhknsw ih puggrur" if operation == 'decrypt' else "Hello World"
            default_key = 'happycoding' if operation == 'decrypt' else 'python'
            # Get the actual input from user
            original_text = input(f'What is the text you want to {operation}? (default = {default_text})\n')
            key = input(f'What is the offset you want to use? (default = {default_key})\n')
            if not key:
                key = default_key
            if not original_text:
                original_text = default_text
            altered_text = encrypt(original_text, key) if operation == 'encrypt' else decrypt(original_text, key)
            print(f'Original text: {original_text} -> Vigenère\'s cypher: {altered_text}')
        case _:
            print('Please run the program again, the only input accepted are the characters: c, C, v,V')

if __name__=='__main__':
    main()
