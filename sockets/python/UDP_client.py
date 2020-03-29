from socket import *

server_name = "localhost"
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
print(client_socket)

while True:
    messsage = input()
    client_socket.sendto(messsage.encode(), (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print(server_address, modified_message.decode())

client_socket.close()
