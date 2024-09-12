import socket
from backend_server_config import backend_servers
from balancing_strategies.round_robin import RoundRobinStrategy
from server_handler import handle_backend_communication


class LoadBalancer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.backend_servers = backend_servers
        self.strategy = RoundRobinStrategy(self.backend_servers)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_socket:
            lb_socket.bind((self.host, self.port))
            lb_socket.listen(10)
            print(f"Load balancer started on {self.host}:{self.port}")

            while True:
                client_socket, client_address = lb_socket.accept()
                backend_server = self.strategy.get_server()
                print(f"Got call from {client_address}: Forwarding request to {backend_server}")
                handle_backend_communication(client_socket, backend_server)

    def add_server(self, server):
        pass


if __name__ == "__main__":
    lb = LoadBalancer("127.0.0.0", 8080)
    lb.start()
    # print('Object lb: ', lb.__dict__)
