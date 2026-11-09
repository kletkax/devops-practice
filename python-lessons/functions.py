def show_status():
    print("Server:OK")
    print("Uptime : 5 days")
#show_status()
#show_status()

def check_server(name):
    print(f"Checking {name}..")
#check_server("web-01")
#check_server("db-01")

def cpu_alert(server_name, cpu):
    if cpu >= 90:
        print(f"[CRITICAL] {server_name}: CPU {cpu}%")
    else:
        print(f"[OK] {server_name}: CPU {cpu}%")
#cpu_alert("db-01", 95)
#cpu_alert("web-01", 40)

def mem_used_percent(total, used):
    return used / total * 100  
memory_used = mem_used_percent(16, 12)
#print(f"Memory used: {memory_used}%")
#if memory_used >= 70:
    #print(f"WARNING: high memory")

servers = [
    {"name": "db-01", "cpu": 95},
    {"name": "cache-01", "cpu": 75},
    {"name": "web-01", "cpu": 40},
]
def get_status(cpu):
    if cpu >= 90:
        return "CRITICAL"
    elif cpu >= 70:
        return "WARNING"
    else:
        return "OK"
for server in servers:
    status = get_status(server['cpu'])
    print(f"[{status}] {server['name']}: CPU {server['cpu']}%")
