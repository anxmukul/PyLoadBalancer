import socket
import sys
import threading
import yaml


class ConfigError(Exception):
    pass


def start_backend_server(host, port):
    print("Starting backend server on {}:{}".format(host, port))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
        backend_socket.bind((host, port))
        backend_socket.listen(3)
        print(f"Backend server listening on {host}:{port}\n")

        while True:
            client_socket, client_address = backend_socket.accept()
            with client_socket:
                print(f"Server on {port}: Connected to {client_address}")
                data = client_socket.recv(4096)
                if data:
                    response = f"Hii from server on{port}: {data.decode()}"
                    client_socket.sendall(response.encode())


def run_servers(backend_server):
    threads = []

    for server in backend_servers:
        host = server["host"]
        port = server["port"]
        thread = threading.Thread(target=start_backend_server, args=(host, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


def load_config():
    try:
        with open("../config.yaml", 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config["backend_servers"]
    except FileNotFoundError:
        raise ConfigError("Configuration file not found. Please check the file path.")
    except KeyError as e:
        raise ConfigError(f"Missing key in configuration: {e}")


if __name__ == "__main__":
    try:
        backend_servers = load_config()
        run_servers(backend_servers)
    except ConfigError as e:
        print(e)
        sys.exit(1)
