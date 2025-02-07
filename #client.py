#client

import socket
import threading

def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{client_address}] {message}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break
    print(f"[-] Connection closed from {client_address}")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("[*] Server listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        clients.add(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    clients = set()
    start_server()
