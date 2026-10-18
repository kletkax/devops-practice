server = input("Server: ")
cpu = int(input("CPU %:"))
if cpu >= 90:
    print(f"[CRITICAL] {server}: CPU {cpu}%")
elif cpu >= 70:
    print(f"[WARNING] {server}: CPU {cpu}%")
else:
    print(f"OK {server}: CPU {cpu}%")
