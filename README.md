[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
![logo](https://github.com/W4RSH3LL/RCE/assets/129652925/317c7ae4-86cd-4ccb-a46f-7617574d9e27)

# Remote Command Execution Tool

This project consists of two Python scripts that enable remote command execution through a backdoor communication mechanism. The listener script sets up a server that waits for incoming connections from the backdoor client. Once a connection is established, various commands can be executed remotely, and files can be uploaded or downloaded.

## Version 1

It is only the first version of this project. It is very buggy, and it still needs some improvement.

## Components

1. **Listener.py**: This Python script waits for incoming connections and allows for remote command execution, file downloads, uploads, and system persistence setup.
2. **Reverse_Backdoor.py**: This Python script connects to the listener and executes received commands, including file operations and system commands.

## Features

- **Command Execution**: Execute any system command on the connected client.
- **File Upload/Download**: Transfer files to and from the connected client.
- **Persistent Access**: Setup commands to maintain persistence on the client system.

## Libraries used in this program 📚📗:!

| Library     | Description                                                                          |
|-------------|--------------------------------------------------------------------------------------|
| `socket`    | Provides low-level networking interface to set up listening server and client sockets. |
| `json`      | Used to encode and decode data into a lightweight data interchange format.            |
| `base64`    | Encodes and decodes binary data to ASCII strings for easy transmission over networks. |
| `subprocess`| Used to execute system commands and retrieve their outputs.                          |
| `os`        | Provides a way to use operating system dependent functionality like reading or writing to a file system. |
| `sys`       | Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. |
| `shutil`    | Offers high-level file operations, particularly file copying and removal.             |

## Installation ✅:
- `git clone https://github.com/W4RSH3LL/RCE.git`
- `cd RCE`
- `pip install -r requirements.txt`

## Usage

### Setting up the Listener

Make sure you modify the attacker_ip and port_to_listen_on in both of the scripts

Run the listener script on the server with an IP address and port number:

```
python3 listener.py
```

## Setting up the Backdoor

Run the backdoor script on the client machine, specifying the server's IP address and port number to establish a connection:

```
python3 reverse_backdoor.py
```

## Commands
- `upload <path>`: Uploads a file to the connected client. (Not working properly yet)
- `download <path>`: Downloads a file from the connected client. (Not working properly yet)
- `persist <path>`: Sets up persistence on the client using the provided path for the executable. (Not working properly yet)
- `cd <directory>`: Changes the current working directory on the client.

## Screenshots 📷:

![image](https://github.com/W4RSH3LL/RCE/assets/129652925/066c93ff-ca6f-4f3b-add4-aac0513e845d)

![image](https://github.com/W4RSH3LL/RCE/assets/129652925/b620803a-5157-4629-9193-16dcfca4928a)

![image](https://github.com/W4RSH3LL/RCE/assets/129652925/cbfb61d8-9259-4e36-9b55-c2e12f17ce6b)

![image](https://github.com/W4RSH3LL/RCE/assets/129652925/3d2607a4-96cf-4702-8365-4e95e5b78b88)


## Disclaimer
This tool is meant for educational purposes only. Use it responsibly and only on devices for which you have proper authorization.

License
This project is released under the MIT License.
