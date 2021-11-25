import statistics as stat
def med(arr,low,high):
    mid = ( high + low )//2
    m = stat.median([arr[low] ,arr[mid],arr[high-1]])
    if m == arr[0]:
        return 0
    elif m == arr[mid]:
        return mid
    else:
        return high-1 
def quick_sort_interface(arr):
    quick_sort(arr, 0, len(arr))
def partition(arr, low, high):
    pivot = med(arr, low, high)
    arr[pivot], arr[low] = arr[low], arr[pivot]
    border = low
    for i in range(len(arr)):
        if arr[i] < arr[0]:
            border+=1
            arr[i], arr[border] = arr[border], arr[i]
            print(arr)
    arr[low], arr[border] = arr[border], arr[low]
    print(border)
    return border

def quick_sort(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        quick_sort(arr, low, part -1)
        quick_sort(arr, part + 1, high)
arr = [0, 2, 10 , 11 ,1 ,4, 5]
print(quick_sort_interface(arr))
print(arr)