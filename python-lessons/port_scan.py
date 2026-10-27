for port in range(20, 26):
    if port == 22:
        print(f"Port 22: open (SSH)")
    else:
        print(f"Port {port}: closed")