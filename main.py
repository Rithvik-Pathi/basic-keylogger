import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller
import os

keyboard = Controller()

def file_checker(key):
    document_path = os.path.expanduser("~\\Documents")
    temp_file = os.path.join(document_path, "temp")

    if os.path.exists(temp_file):
        with open(temp_file, "a"):
            print(f"found existing file, writing to {temp_file}")
    else:
        open(temp_file, "xt")
        print(f"Creating a file at {document_path}")




file_checker(key=Key.media_play_pause)