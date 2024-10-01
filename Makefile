# Makefile for PyLoadBalancer

.PHONY: all start_bs start_lb start_client close

run: start_bs start_lb start_client

start_bs:
	@echo "Starting backend servers..."
	cd backend && python3 backend_server.py &

start_lb:
	@echo "Starting load balancer..."
	cd src && python3 load_balancer.py &

start_client:
	@echo "Starting client..."
	cd client && python3 client.py

close_lb:
	@echo "closing load balancer.."
	pkill -f "load_balancer.py" || true

close_bs:
	@echo "closing backend_server..."
	pkill -f "backend_server.py" || true

