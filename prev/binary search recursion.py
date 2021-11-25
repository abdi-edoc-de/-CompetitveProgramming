def binary_search(arr,l,r,target):
    if r >= l:
        mid = (r + l )//2 
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            return binary_search(arr, l, mid-1, target)
        else:
            return binary_search(arr, mid+1, r, target)
    return -1
arr = [1, 2, 3, 44, 50, 89]
print(binary_search(arr, 0, len(arr), 50))
