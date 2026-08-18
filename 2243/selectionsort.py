n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    element=int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Original array:", arr)

# Selection sort
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"After pass {i+1}: {arr}")

print("Sorted array:", arr)

# Top five elements
top_five = arr[-5:] if n >= 5 else arr


print("Top five elements:", top_five)