port = int(input("Port:"))
if port == 22:
    print("SSH")
elif port == 80:
    print("HTTP")
elif port == 443:
    print("HTTPS")
else:
    print(f"Unknown port {port}")