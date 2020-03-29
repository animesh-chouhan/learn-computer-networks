from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(("localhost", server_port))
print(f"* Server started at port {server_port}")

while True:
    message, client_address = server_socket.recvfrom(2048)
    print(client_address, message.decode())
    modified_message = message.upper()
    server_socket.sendto(modified_message, client_address)
