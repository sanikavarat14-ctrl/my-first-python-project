def binary_search(account_ids, target):
    left, right = 0, len(account_ids) - 1

    while left <= right:
        mid = (left + right) // 2
        if account_ids[mid] == target:
            return mid  
        elif account_ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  


ids = [1001, 1050, 2200, 3450, 5000]
print(binary_search(ids, 2200))  