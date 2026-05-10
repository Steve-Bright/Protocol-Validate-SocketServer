import socket  # import socket module for network communication

def sendMessage(message):
    # define the server IP address
    SERVER_HOST = "127.0.0.1"

    # define the server port number
    SERVER_PORT = 5000

    # create a UDP socket using IPv4 addressing
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # display the message that will be sent
    print("Sending the message:", message)

    # send encoded message to the server address and port
    client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

    # receive response data from server with maximum size of 1024 bytes
    data, server_address = client_socket.recvfrom(1024)

    # decode received bytes into readable string
    response = data.decode()

    # display the response received from the server
    print("Server response:", response)

    # close the client socket connection
    client_socket.close()

# check whether this file is being run directly
if __name__ == "__main__":
    try:
        # continuously ask user for input until stopped
        while True:

            # prompt user to enter a message
            toSend = input("Enter message: ")

            # if user types "exit", stop the loop
            if toSend.lower() == "exit":
                break

            # check that input is not empty
            if toSend:

                # send the entered message to the server
                sendMessage(toSend)

    # handle Ctrl + C interruption from keyboard
    except KeyboardInterrupt:

        # display shutdown message
        print("\nClient shutting down...")