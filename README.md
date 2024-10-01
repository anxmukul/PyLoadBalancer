# Python Load Balancer

## Overview
PyBalancer is a custom load balancer implemented from scratch in Python. It listens for client connections and distributes requests across multiple backend servers to balance the load and optimize resource usage.

## Features
- Multiple backend servers, Easy-to-configure backend servers
- Graceful shutdown of servers
- Supports different load balancing algorithms.
- Logging for better observability


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
   ```

## Usage
1. Start the backend servers, load balancer, and client using make:
   ```bash
   make run
   ```
   This command will:
   Start 3 backend servers on ports 8001, 8002, and 8003.
   Start the load balancer, which will distribute traffic among the backend servers.
   Simulate client requests.

2. Stop the servers and clean up:
   ```bash
   make close
   ```
3. You can stop each one of them using these command:
   ```bash
   make close_lb
   make close_bs
   make close_client
   ```


