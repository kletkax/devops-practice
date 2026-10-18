count = int(input("How many servers you want to check? - "))

for i in range(1, count + 1):
    if i % 2 == 0:
        print(f"web-{i}: OK")
    else:
        print(f"web-{i}: CHECK")
print(f"Checked {count} servers")