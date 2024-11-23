import socket
import time

# Set up the client (User B)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

try:
    message_count = 1
    while True:  # Infinite loop to keep sending messages
        message = f"Hello from User B! Message {message_count}"
        client_socket.send(message.encode())
        print(f"Sent to User A (Server): {message}")
        message_count += 1
        time.sleep(2)  # Wait 2 seconds before sending the next message
except KeyboardInterrupt:
    print("Client closed by user.")
finally:
    client_socket.close()
