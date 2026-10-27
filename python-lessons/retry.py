server = "db-01"
max_attempts = int(input("Max attempts: "))
attempt = 1
while attempt <= max_attempts:
    print(f"Attempt {attempt}/{max_attempts}: connecting to {server}...")
    attempt += 1
print(f"Failed after {max_attempts} attempts")