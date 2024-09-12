import socket


def handle_backend_communication(client_socket, backend_server):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
        backend_socket.connect(backend_server)

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            backend_socket.sendall(data)

            response = backend_socket.recv(1024)
            client_socket.sendall(response)

        client_socket.close()
