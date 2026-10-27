server = input("Server name: ")
disk_count = int(input("Disks count: "))
for i in range(1, disk_count + 1):
    used = int(input(f"Disk {i} used %: "))
    if used >= 90:
        print(f"[CRITICAL] {server} disk {i}: {used}git add disk_alert.py
git commit -m "lesson 5: disk_alert.py"
git push
    elif used >= 75:
        print(f"[WARNING] {server} disk {i}: {used} ")
    else:
        print(f"[OK] {server} disk {i}: {used} ")
print(f"Checked {disk_count} disks on {server}")

