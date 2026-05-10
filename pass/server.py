import socket  # import socket module for network communication

# define the server IP address
HOST = "127.0.0.1"

# define the server port number
PORT = 5000

# define the required message header format
HEADER = "TNE20003:"

# create a UDP socket using IPv4 addressing
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# display message showing server is running
print(f"UDP server running on {HOST}:{PORT}")

# continuously wait for client messages
while True:

    # recvfrom() is used for UDP communication
    # receives data and the sender's address
    data, client_address = server_socket.recvfrom(1024)

    # recvfrom() returns a tuple:
    # data = received bytes
    # client_address = sender IP address and port number

    # decode received bytes into readable string
    message = data.decode()

    # display received message from client
    print("Received from client:", message)

    # check whether message starts with correct header
    # and ensure message contains text after the header
    if message.startswith(HEADER) and len(message) > len(HEADER):

        # extract actual message after the header
        actual_message = message[len(HEADER):]

        # create success response message
        response = "TNE20003:A:" + actual_message

    else:
        # create error response for invalid message format
        response = "TNE20003:E:Invalid message format"

    # send encoded response back to the client address
    server_socket.sendto(response.encode(), client_address)