## Pass point
### Client
Sends a UDP message to the server, waits for a response, and displays the returned message.

### Server
Receives UDP messages from clients, validates the message format, and sends a success or error response back to the client.

---

## Credit point
Credit point has two versions. One client1 and server1 is intended way by the lab tutor. 
They are upgraded to robust server and client by checking the "Enter Escape": "\n". However, their basic goals remain the same.

### Client
Establishes a TCP connection with the server, sends a message, waits for the server response, and displays the returned message.

### Server
Accepts TCP client connections, receives messages, validates the message format, and sends a success or error response back to the client.
