import socket
import sys

import yaml

from balancing_strategies.round_robin import RoundRobinStrategy
from server_handler import handle_backend_communication


class LoadBalancer:
    def __init__(self, host, port, servers):
        self.host = host
        self.port = port
        self.backend_servers = servers
        self.strategy = RoundRobinStrategy(self.backend_servers)

    def start(self):
        print(f"Starting load balancer on {self.host}:{self.port}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_socket:
            lb_socket.bind((self.host, self.port))
            lb_socket.listen(10)
            print(f"Load balancer started on {self.host}:{self.port}")

            while True:
                client_socket, client_address = lb_socket.accept()
                backend_server = self.strategy.get_server()
                print(f"Got a client: {client_address}: assigning server {backend_server}")
                handle_backend_communication(client_socket, backend_server)


class ConfigError(Exception):
    pass


def load_config():
    try:
        with open('../config.yaml', 'r') as config_file:
            parsed_config = yaml.safe_load(config_file)
        return parsed_config["backend_servers"], parsed_config["load_balancer"]
    except FileNotFoundError:
        raise ConfigError("Configuration file not found. Please check the file path.")
    except KeyError as e:
        raise ConfigError(f"Missing key in configuration: {e}")


if __name__ == "__main__":
    try:
        backend_servers, load_balancer = load_config()
        print(f"Configuration from YAML file is {backend_servers}, {load_balancer}")
        backend_servers = [(server["host"], server["port"]) for server in backend_servers]
        lb = LoadBalancer(load_balancer["host"], load_balancer["port"], backend_servers)
        lb.start()
    except ConfigError as e:
        print(e)
        sys.exit(1)
