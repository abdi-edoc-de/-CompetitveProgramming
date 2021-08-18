arr = [0, 2, 2, 1, 1, 0, -5, 3]
print(len(arr))
# print(arr[len(arr)])
swap = True
while swap:
    swap= False
    for i in range(len(arr)):
        if i < len(arr)-1 and arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            swap = True
print(arr)