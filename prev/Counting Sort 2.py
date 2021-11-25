
def countingSort(arr):
    # Write your code here
    max = arr[0]
    for i in arr:
        if i > max:
            max=i
    arr2=[]
    for i in range(max+1):
        arr2.append(0)

    for i in arr:
        arr2[i]+=1
    arr=[]
    for i in range(len(arr2)):
        for j in range(arr2[i]):
            arr.append(i)
    return arr
arr = [0, 2, 2, 1, 1, 0, 3]

print(countingSort(arr))

