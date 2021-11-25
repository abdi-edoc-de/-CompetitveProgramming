def binarySearcch(arr, l, r, target):
    while l <= r:
        mid =l+ (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
arr = [-1,0,3,5,9,12]

print(binarySearcch(arr, 0, len(arr)-1, 9))