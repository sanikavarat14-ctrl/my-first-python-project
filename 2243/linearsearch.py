n = int(input("Enter the number of IDs: "))

ids = []

for i in range(n):
    value = int(input(f"Enter ID {i + 1}: "))
    ids.append(value)

search_id = int(input("Enter the ID to search: "))

found = False

for i in range(n):
    if ids[i] == search_id:
        print("ID found at position", i + 1)
        found = True
        break

if not found:
    print("ID not found.")   