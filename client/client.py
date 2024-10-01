import socket
import time

import yaml


def call_load_balancer(host, port, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(msg.encode())
        response = client_socket.recv(1024)
        print(f"Received: {response}")


class ConfigError(Exception):
    pass


def wait_for_load_balancer(host, port, max_attempts=5):
    for attempts in range(max_attempts):
        print("Trying to connect with load balancer...")
        try:
            with socket.create_connection((host, port), timeout=1):
                print("Load balancer is ready!")
                return
        except (ConnectionRefusedError, OSError):
            print("Waiting for load balancer...")
            time.sleep(2)
    print("Failed to connect to load balancer after several attempts.")
    exit(1)


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
        wait_for_load_balancer(load_balancer_config["host"], load_balancer_config["port"], 5)
        for i in range(555):
            call_load_balancer(load_balancer_config["host"], load_balancer_config["port"], f"Request from client {i}")
    except ConfigError as e:
        print(e)
        exit(1)
