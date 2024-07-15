from functions import decrypt_message, encrypt_message, keys_dict

message = input('Write here the message to be encrypted: ')

encrypted_message = encrypt_message(message, keys_dict)
print(f'Encrypted message: {type(encrypted_message)}')

decrypted_message = decrypt_message(encrypted_message, keys_dict)
print(f'Decrypted message: {type(decrypted_message)}')