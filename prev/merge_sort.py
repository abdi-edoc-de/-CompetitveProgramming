def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        l = r = c = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[c] = left[l]
                l +=1 
            else:
                arr[c] = right[r]
                r+=1
            c+=1
        while l < len(left):
            arr[c] = left[l]
            l+=1
            c+=1
        while r < len(right):
            arr[c] = right[r]
            r +=1 
            c+=1
        
arr = [4,3,5,1,-3,4,123,4,34]
merge_sort(arr)
print(arr)
print(114 // 10 ** 3 % 10)
