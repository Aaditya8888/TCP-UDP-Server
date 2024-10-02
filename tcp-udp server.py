#!usr/bin/python3
import socket
import threading
import time

# Define the banner message
BANNER = """
***********************************************
*     Welcome. This is secure server           *
*     All activity is monitored!               *
***********************************************
"""

print(BANNER)
time.sleep(1)
# TCP client handler
def handle_tcp_client(client_socket):
    # Send banner and current time to the client
    client_socket.send(BANNER.encode())
    client_socket.send(f"Current server time: {time.ctime()}\n".encode())

    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received from TCP client: {message.decode('utf-8')}")
            client_socket.send(b"Message received (TCP)")
        except ConnectionResetError:
            break

    client_socket.close()

# UDP client handler
def handle_udp_client(server_socket):
    while True:
        message, client_addr = server_socket.recvfrom(1024)
        print(f"Received from UDP client: {message.decode('utf-8')} from {client_addr}")
        server_socket.sendto(b"Message received (UDP)", client_addr)

# TCP server setup
def start_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 65432))
    server.listen(5)
    print("TCP Server started on port 65432...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted TCP connection from {addr}")
        client_handler = threading.Thread(target=handle_tcp_client, args=(client_socket,))
        client_handler.start()

# UDP server setup
def start_udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 65433))
    print("UDP Server started on port 65433...")

    # Handle incoming data in the main thread
    handle_udp_client(server)

# Main server selector
def start_server():
    print("Select the service you want to start:")
    print("1. TCP Service")
    print("2. UDP Service")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        start_tcp_server()
    elif choice == "2":
        start_udp_server()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    start_server()



