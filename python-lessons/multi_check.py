servers_count = int(input("Enter the number of servers: "))
critical = 0
while servers_count <= 0:
    print("Need at least 1 server")
    servers_count = int(input("Enter the number of the servers:"))
for i in range(1, servers_count + 1):
    server_name = input(f"Enter the name of the server {i}:")
    cpu_server = int(input("Cpu in %:"))
    if cpu_server >= 90:
        print(f"[CRITICAL] {server_name}: CPU {cpu_server}%")
        critical += 1
    elif cpu_server >= 70:
        print(f"[WARNING] {server_name}: CPU {cpu_server}%")
    else:
        print(f"[OK] {server_name}: CPU {cpu_server}%")
print(f"Checked {servers_count}, critical: {critical}")
