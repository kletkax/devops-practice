ports = [22, 80, 22, 443, 80, 8080]
   

unique_ports = set(ports)
print(f"Total: {len(ports)}")
print(f"Unique: {len(unique_ports)}")
services = {22: "SSH", 80: "HTTP", 443: "HTTPS"}
for port in unique_ports:
    print(f"{port}: {services.get(port, 'Unknown')}")