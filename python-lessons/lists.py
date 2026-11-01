servers = ["db-01", "web-01", "cache-01"]
servers.append("backup-01")
print(servers[0])
print(servers[1])
print(servers[-1])
print(len(servers))
for server in servers:
    print(f"Checking {server}..")
print(servers)
print(len(servers))