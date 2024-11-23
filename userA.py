import socket

# Set up the server (User A)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("User A (Server) listening for connections...")

# Accept a connection from the client (User B)
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

try:
    while True:  # Infinite loop to keep receiving messages
        data = client_socket.recv(1024).decode()
        if not data:
            print("No data received. Waiting for the next message...")
            continue  # Continue listening if no data is received
        print(f"Received from User B (Client): {data}")
except KeyboardInterrupt:
    print("Server closed by user.")
finally:
    client_socket.close()
    server_socket.close()
