import socket  # import socket module for network communication

# define the server IP address
HOST = "127.0.0.1"

# define the server port number
PORT = 5000

# define the required message header format
HEADER = "TNE20003:"


# function to validate and process received message
def checkMessage(client_socket, message):

    # display received message from client
    print("Received from client:", message)

    # check whether message starts with correct header
    # and ensure there is text after the header
    if message.startswith(HEADER) and len(message) > len(HEADER):

        # extract actual message after the header
        actual_message = message[len(HEADER):]

        # create success response message
        response = "TNE20003:A:" + actual_message

    else:
        # create error response for invalid format
        response = "TNE20003:E:Invalid message format"

    # encode and send response back to client
    client_socket.send(response.encode())


# main function to run the TCP server
def main():

    # create a TCP socket using IPv4 addressing
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to the specified host and port
    server_socket.bind((HOST, PORT))

    # enable the socket to accept incoming connections
    server_socket.listen()

    # display message showing server is running
    print(f"TCP server running on {HOST}:{PORT}")

    # continuously wait for client connections
    while True:

        # create empty bytes variable to store received message
        message = b""

        # accept incoming client connection
        # returns a new socket for the connected client
        # and the client's address information
        client_socket, client_address = server_socket.accept()

        # display connected client address
        print(f"Connected to client: {client_address}")

        # continuously receive data from client
        while True:

            # receive up to 1024 bytes from client
            data = client_socket.recv(1024)

            # stop loop if no more data is received
            if not data:
                break

            # append received data into message variable
            message += data

        # decode received bytes and validate message
        checkMessage(client_socket, message.decode())

        # close connection with the client
        client_socket.close()


# check whether this file is being run directly
if __name__ == "__main__":

    # start the server
    main()