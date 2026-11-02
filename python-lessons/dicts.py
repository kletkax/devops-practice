server = {
    "name": "db-01",
    "port": 5432,
    "cpu": 85
}
print(server["name"])
print(server["cpu"])
print(f"Server {server['name']} uses port {server['port']}")





server["cpu"] = 95
server["status"] = "UP"
print(server)

print(server.get("ram", "unknown"))
print(server.get("cpu", "unknown"))