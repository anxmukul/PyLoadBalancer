import socket
import threading


def start_backend_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
        backend_socket.bind((host, port))
        backend_socket.listen(3)
        print(f"Backend server listening on {host}:{port}\n")

        while True:
            client_socket, client_address = backend_socket.accept()
            with client_socket:
                print(f"Connected to {client_address}")
                data = client_socket.recv(4096)
                if data:
                    response = f"Response from backend {port}: {data.decode()}"
                    client_socket.sendall(response.encode())


def run_servers(host, backend_server_ports):
    threads = []

    for b_port in backend_server_ports:
        thread = threading.Thread(target=start_backend_server, args=(host, b_port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = [8001, 8002, 8003]
    run_servers(host, port)
