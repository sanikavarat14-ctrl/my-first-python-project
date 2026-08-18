n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    element=int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Original array:", arr)

# Bubble sort
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"After pass {i+1}: {arr}")

print("Sorted array:", arr)     

# Top five elements
top_five = arr[-5:] if n >= 5 else arr
print("Top five elements:", top_five)