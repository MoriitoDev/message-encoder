import dearpygui.dearpygui as dpg
import pyperclip
from functions import *

dpg.create_context()
dpg.create_viewport(title='Message Encryptor', width=600, height=300)

encripted_dict = {}
decripted_dict = {}

def encrypt_button_encrypt_message(sender, app_data, user_data):
    input_value = dpg.get_value("input_field")  # This gets the input value
    dpg.set_value("input_field", "")  # Clears the input value
    encrypted_message = encrypt_message(message=input_value, keys_dict=keys_dict)
    encripted = encrypted_message
    dpg.set_value("output_text", f"Saved Input: {encrypted_message}")
    return encripted

def encrypt_decrypt():
    input_value = dpg.get_value("input_field")
    dpg.set_value("input_field", "")
    encrypted_message = encrypt_message(message=input_value, keys_dict=keys_dict)
    decrypted_message = decrypt_message(encrypted_message=encrypted_message, keys_dict=keys_dict)
    dpg.set_value("output_text", f"Encrypted message: {encrypted_message} \nDecrypted message: {decrypted_message}")
    encripted_dict.update({"encripted_value" : encrypted_message})
    decripted_dict.update({"decrypted_value" : decrypted_message})

def encrypt_copytoclipboard():
    pyperclip.copy(encripted_dict['encripted_value'])

def decrypt_copytoclipboard():
    pyperclip.copy(decripted_dict['decrypted_value'])

with dpg.window(label="Message Encryptor", tag="encrypt_window", autosize=True):
    dpg.add_text("Here you can encrypt your message.")
    dpg.add_input_text(label="Input Field", hint="Enter text here", tag="input_field")
    dpg.add_button(label="Encrypt!", callback=encrypt_decrypt)
    dpg.add_text(default_value="Encrypted message: None \nDecrypted message: None", tag="output_text")
    dpg.add_button(label="Copy encripted", callback=encrypt_copytoclipboard)
    dpg.add_button(label="Copy decrypted", callback=decrypt_copytoclipboard)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()