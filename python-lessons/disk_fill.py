disk = 60
minute = 1
while disk < 100:
    print(f"Minute {minute}: disk {disk}%")
    disk += 10
    minute += 1
print("Disk full!")