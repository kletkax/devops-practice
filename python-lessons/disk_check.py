disk_used = int(input("disk used %:"))
if disk_used > 90:
    print("Alert: disk almost full")
elif disk_used >= 75:
    print("Warning, disk filling up")
else:
    print("Everything is alr")
print("Check done")