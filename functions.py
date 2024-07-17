import secrets
import pickle

char_dict = {    'a': 'a',    'b': 'b',    'c': 'c',    'd': 'd',    'e': 'e',    'f': 'f',    'g': 'g',    'h': 'h',    'i': 'i',    'j': 'j',    'k': 'k',    'l': 'l',    'm': 'm',    'n': 'n',    'o': 'o',    'p': 'p',    'q': 'q',    'r': 'r',    's': 's',    't': 't',    'u': 'u',    'v': 'v',    'w': 'w',    'x': 'x',    'y': 'y',    'z': 'z',    'A': 'A',    'B': 'B',    'C': 'C',    'D': 'D',    'E': 'E',    'F': 'F',    'G': 'G',    'H': 'H',    'I': 'I',    'J': 'J',    'K': 'K',    'L': 'L',    'M': 'M',    'N': 'N',    'O': 'O',    'P': 'P',    'Q': 'Q',    'R': 'R',    'S': 'S',    'T': 'T',    'U': 'U',    'V': 'V',    'W': 'W',    'X': 'X',    'Y': 'Y',    'Z': 'Z',    '0': '0',    '1': '1',    '2': '2',    '3': '3',    '4': '4',    '5': '5',    '6': '6',    '7': '7',    '8': '8',    '9': '9',    '!': '!',    '"': '"',    '#': '#',    '$': '$',    '%': '%',    '&': '&',    "'": "'",    '(': '(',    ')': ')',    '*': '*',    '+': '+',    ',': ',',    '-': '-',    '.': '.',    '/': '/',    ':': ':',    ';': ';',    '<': '<',    '=': '=',    '>': '>',    '?': '?',    '@': '@',    '[': '[',    '\\': '\\',    ']': ']',    '^': '^',    '_': '_',    '': '',    '{': '{',    '|': '|',    '}': '}',    '~': '~',    ' ': ' '}

keys_dict = {}

# Generar una clave para cada letra y almacenarla en keys_dict
for x in char_dict:
    token_key = secrets.token_bytes(16)
    keys_dict[x] = token_key

# Guardar keys_dict en un archivo
with open('keys_dict.pkl', 'wb') as f:
    pickle.dump(keys_dict, f)

# Cargar keys_dict del archivo
with open('keys_dict.pkl', 'rb') as f:
    keys_dict = pickle.load(f)

def encrypt_message(message, keys_dict):
    encrypted_message = b""  # Inicializa como una cadena de bytes vacía
    for char in message:
        if char in keys_dict:
            encrypted_message += keys_dict[char]
        else:
            encrypted_message += char.encode()  # Si el carácter no está en el diccionario, se deja sin cambios
    return encrypted_message

def decrypt_message(encrypted_message, keys_dict):
    decrypted_message = ""
    key_length = 16  # Longitud de las claves en bytes
    for i in range(0, len(encrypted_message), key_length):
        key_segment = encrypted_message[i:i+key_length]
        for char, key in keys_dict.items():
            if key == key_segment:
                decrypted_message += char
                break
        else:
            decrypted_message += key_segment.decode()  # If no key, no changes applied
    return decrypted_message