import dearpygui.dearpygui as dpg
import pyperclip
from functions import *

dpg.create_context()
dpg.create_viewport(title='Message Encryptor', width=600, height=300)

encripted = b""
decripted = ""

def encrypt_button_encrypt_message(sender, app_data, user_data):
    input_value = dpg.get_value("input_field")  # This gets the input value
    dpg.set_value("input_field", "")  # Clears the input value
    encrypted_message = encrypt_message(message=input_value, keys_dict=keys_dict)
    encripted = encrypted_message
    dpg.set_value("output_text", f"Saved Input: {encrypted_message}")
    return encripted

# Function to copy the output text to clipboard
def encripted_button_copy_to_clipboard(sender, app_data, user_data):
    pyperclip.copy(encripted)

def decrypt_button_message(sender, app_data, user_data):
    input_value = dpg.get_value("decrypt_input_field")  # This gets the input value
    dpg.set_value("decrypt_input_field", "")  # Clears the input value
    decripted_message = decrypt_message(encrypted_message=encripted, keys_dict=keys_dict)
    input_value.update({"decripted_message": decripted_message})
    dpg.set_value("decrypt_output_text", f"Saved Input: {decripted_message}")
    return decripted_message

def decrypted_button_copy_to_clipboard(sender, app_data, user_data):
    pyperclip.copy(decripted)

with dpg.window(label="Encrypt", tag="encrypt_window", autosize=True):
    dpg.add_text("Here you can encrypt your message.")
    dpg.add_input_text(label="Input Field", hint="Enter text here", tag="input_field")
    dpg.add_button(label="Encrypt!", callback=encrypt_button_encrypt_message)
    dpg.add_text(default_value="Saved Input: None", tag="output_text")
    dpg.add_button(label="Copy to Clipboard", callback=encripted_button_copy_to_clipboard)

with dpg.window(label="Decrypt", tag="decrypt_window", autosize=True):
    dpg.add_text("Here you can decrypt your message.")
    dpg.add_input_text(label="Input Field", hint="Enter text here", tag="decrypt_input_field")
    dpg.add_button(label="Decrypt!", callback=decrypt_button_message)
    dpg.add_text(default_value="Saved Input: None", tag="decrypt_output_text")
    dpg.add_button(label="Copy to Clipboard", callback=decrypted_button_copy_to_clipboard)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
