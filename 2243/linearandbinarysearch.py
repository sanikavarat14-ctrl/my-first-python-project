print("1. Linear Search")
print("2. Binary Search")

option = int(input("Enter option: "))

if option == 1:

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

elif option == 2:

    n1 = int(input("Enter the number of IDs: "))
    ids1 = []

    for i in range(n1):
        value = int(input(f"Enter ID {i + 1}: "))
        ids1.append(value)

    ids1.sort()

    print("Sorted IDs:", ids1)

    search_id = int(input("Enter the ID to search: "))

    low = 0
    high = n1 - 1
    found = False

    while low <= high:
        mid = (low + high) // 2

        if ids1[mid] == search_id:
            print("ID found at position", mid + 1)
            found = True
            break
        elif ids1[mid] < search_id:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print("ID not found.")

else:
    print("Invalid option.")