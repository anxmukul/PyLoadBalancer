# Python Load Balancer

## Overview
PyBalancer is a custom load balancer implemented from scratch in Python. It listens for client connections and distributes requests across multiple backend servers to balance the load and optimize resource usage.

## Features
- Multiple backend servers, Easy-to-configure backend servers
- Graceful shutdown of servers
- Supports different load balancing algorithms.
- Logging for better observability

## Project Structure
load_balancer_project/ │ ├── src/ │ ├── init.py │ ├── load_balancer.py │ ├── server_handler.py │ ├── health_check.py │ └── balancing_strategies/ │ ├── init.py │ ├── round_robin.py │ ├── least_conn.py │ └── ip_hash.py │ ├── tests/ │ ├── init.py │ ├── test_load_balancer.py │ └── test_health_check.py │ ├── Makefile └── README.md


## Requirements
- Python 3.12.3
- Install dependencies via `requirements.txt`:

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PyLoadBalancer.git
   cd PyLoadBalancer
   ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
   ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt


    





