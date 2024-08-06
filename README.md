# Socket Real-Time Chat Application

This is a simple real-time chat application built using Python's socket module. It allows multiple clients to connect to a server and send messages to each other in real-time.

## Features

- Multiple clients can connect to the server simultaneously.
- Real-time message broadcasting to all connected clients.
- User-friendly command-line interface for sending and receiving messages.

## Prerequisites

- Python 3.x installed on your system.

## Files

- `server.py`: The server-side script that handles incoming client connections and message broadcasting.
- `client1.py`: The client-side script for the first client.
- `client2.py`: The client-side script for the second client.

## Usage

### 1. Running the Server

1. Open a terminal.
2. Navigate to the directory where `server.py` is located.
3. Run the server script:

```bash
python server.py
```

The server will start and wait for client connections.

### 2. Running the Clients

1. Open a new terminal for each client.
2. Navigate to the directory where `client1.py` or `client2.py` is located.
3. Run the client script:

```bash
python client1.py
```

or

```bash
python client2.py
```

Each client will connect to the server and you can start sending messages.

## How It Works

### Server (`server.py`)

- Listens for incoming client connections on a specified port.
- Accepts new connections and creates a new thread for each client.
- Receives messages from clients and broadcasts them to all connected clients.

### Client (`client1.py` and `client2.py`)

- Connects to the server.
- Sends user input messages to the server.
- Receives and displays broadcasted messages from the server.

## Example

1. Start the server:

```bash
python server.py
```

Output:
```
Server started, waiting for connections...
```

2. Start the first client:

```bash
python client1.py
```

Output:
```
Enter your name: Alice
Welcome to the chat, Alice!
```

3. Start the second client:

```bash
python client2.py
```

Output:
```
Enter your name: Bob
Welcome to the chat, Bob!
```

4. Alice sends a message:

```
Alice: Hello, Bob!
```

5. Bob receives the message:

```
Alice: Hello, Bob!
```

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. Any enhancements or bug fixes are welcome.



## Contact

For any questions or suggestions, please contact Omar Ahmed Mohamed at [omarref3at2031@gmail.com].

---

Happy chatting!
```
