import socket


class LoadBalancer:
    def __init__(self, host, port, backend_servers):
        self.host = host
        self.port = port
        self.backend_servers = backend_servers

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_socket:
            lb_socket.bind((self.host, self.port))
            lb_socket.listen(10)
            print(f"Load balancer started on {self.host}:{self.port}")

    def add_server(self, server):
        pass


if __name__ == "__main__":
    backend_server = [("127.0.0.1", 8001), ("127.0.0.1", 8002)]
    lb = LoadBalancer("0.0.0.0", 8080, backend_server)
    lb.start()
    # print('Object lb: ', lb.__dict__)
