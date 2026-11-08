servers = [
    {"name": "db-01", "cpu": 95},
    {"name": "cache-01", "cpu": 75},
    {"name": "web-01", "cpu": 40},

]
for server in servers:
    if server["cpu"] >= 90:
        print(f"[CRITICAL] {server['name']}: CPU {server['cpu']}%")
    elif server["cpu"] >= 70:
        print(f"[WARNING] {server['name']}: CPU {server['cpu']}%")
    else:
        print(f"[OK] {server['name']}: CPU {server['cpu']}%")