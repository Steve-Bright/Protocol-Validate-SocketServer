import socket

HOST = "127.0.0.1"
PORT = 5000
HEADER = "TNE20003:"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"TCP server running on {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()

    print("Connected:", client_address)

    buffer = ""

    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        buffer += data.decode()

        while "\n" in buffer:
            message, buffer = buffer.split("\n", 1)

            print("Received:", message)

            if message.startswith(HEADER) and len(message) > len(HEADER):
                actual_message = message[len(HEADER):]
                response = "TNE20003:A:" + actual_message
            else:
                response = "TNE20003:E:Invalid message format"

            client_socket.send((response + "\n").encode())

    client_socket.close()