import socket


def call_load_balancer(host, port, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(msg.encode())
        response = client_socket.recv(1024)
        print(f"Received: {response}")


if __name__ == "__main__":
    lb_host = "127.0.0.0"
    lb_port = 8080

    for i in range(10):
        call_load_balancer(lb_host, lb_port, f"Request from client {i}")
