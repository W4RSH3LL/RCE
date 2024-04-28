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
- upload <path>: Uploads a file to the connected client.
- download <path>: Downloads a file from the connected client.
- persist <path>: Sets up persistence on the client using the provided path for the executable.
- cd <directory>: Changes the current working directory on the client.

## Disclaimer
This tool is meant for educational purposes only. Use it responsibly and only on devices for which you have proper authorization.

License
This project is released under the MIT License.
