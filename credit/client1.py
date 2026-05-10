import socket  # import socket module for network communication

# define the server IP address
SERVER_HOST = "127.0.0.1"

# define the server port number
SERVER_PORT = 5000

def sendMessage(message):

    # create a TCP socket using IPv4 addressing
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish TCP connection with the server
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # display the message being sent
    print("Sending message:", message)

    # encode and send message to the server
    client_socket.send(message.encode())

    # indicate that the client has finished sending data
    client_socket.shutdown(socket.SHUT_WR)

    # create empty bytes variable to store server response
    response = b""

    # continuously receive data from server
    while True:

        # receive up to 1024 bytes from server
        data = client_socket.recv(1024)

        # stop loop if no more data is received
        if not data:
            break

        # append received data into response variable
        response += data

    # decode and display the server response
    print("Server response:", response.decode())

    # close the client socket connection
    client_socket.close()


# check whether this file is being run directly
if __name__ == "__main__":
    try:

        # continuously ask user for input
        while True:

            # prompt user to enter message
            toSend = input("Enter message: ")

            # stop loop if user types "exit"
            if toSend.lower() == "exit":
                break

            # ensure message is not empty
            if toSend:

                # send entered message to server
                sendMessage(toSend)

    # handle Ctrl + C interruption
    except KeyboardInterrupt:

        # display shutdown message
        print("\nClient shutting down...")