import time
import random

# ---------------------------------------------------------
# 1. The "Servers" (Backends)
# ---------------------------------------------------------
class Server:
    def __init__(self, name):
        self.name = name

    def handle_request(self, request_id):
        print(f"  [{self.name}] 🟢 Processing Request #{request_id}...")
        # Simulate work
        time.sleep(0.5)
        return "200 OK"

# ---------------------------------------------------------
# 2. The Load Balancer
# ---------------------------------------------------------
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0  # Pointer to track whose turn it is

    def get_next_server(self):
        # ROUND ROBIN ALGORITHM
        # 1. Pick the current server
        server = self.servers[self.current_index]

        # 2. Move the pointer to the next server
        # The '%' operator makes it loop back to 0 when we reach the end
        self.current_index = (self.current_index + 1) % len(self.servers)

        return server

# ---------------------------------------------------------
# 3. The Traffic Simulation
# ---------------------------------------------------------
if __name__ == "__main__":
    # We have 3 backend servers
    backend_fleet = [
        Server("Server-A (US-East)"),
        Server("Server-B (US-West)"),
        Server("Server-C (EU-Central)")
    ]

    lb = LoadBalancer(backend_fleet)

    print("--- TRAFFIC SPIKE INCOMING (10 Requests) ---")

    # Simulate 10 users hitting the site at once
    for i in range(1, 11):
        # Ask the Load Balancer: "Who should handle this?"
        assigned_server = lb.get_next_server()
        assigned_server.handle_request(i)

    print("\n--- ALL REQUESTS HANDLED ---")
