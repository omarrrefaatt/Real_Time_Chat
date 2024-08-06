import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        message = input('')
        client_socket.send(message.encode('utf-8'))

# Set up the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

send_thread = threading.Thread(target=send_messages, args=(client,))
send_thread.start()
