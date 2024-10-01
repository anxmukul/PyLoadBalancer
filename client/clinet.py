import socket
import yaml


def call_load_balancer(host, port, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(msg.encode())
        response = client_socket.recv(1024)
        print(f"Received: {response}")


class ConfigError(Exception):
    pass


def load_config():
    try:
        with open("../config.yaml", 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config["load_balancer"]
    except FileNotFoundError:
        raise ConfigError("Configuration file not found. Please check the file path.")
    except KeyError as e:
        raise ConfigError(f"Missing key in configuration: {e}")


if __name__ == "__main__":
    try:
        load_balancer_config = load_config()

        for i in range(10):
            call_load_balancer(load_balancer_config["host"], load_balancer_config["port"], f"Request from client {i}")
    except ConfigError as e:
        print(e)
        exit(1)
