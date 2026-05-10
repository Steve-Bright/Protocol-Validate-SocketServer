import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((SERVER_HOST, SERVER_PORT))

try:
    while True:
        message = input("Enter message: ")

        if message.lower() == "exit":
            break

        full_message = message + "\n"

        client_socket.send(full_message.encode())

        response = client_socket.recv(1024).decode()

        print("Server response:", response.strip())

finally:
    client_socket.close()