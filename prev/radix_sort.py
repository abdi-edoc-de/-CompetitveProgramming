from functools import reduce
def radix_sort(arr):
    num_of_digits = len(str(max))
    for dgt in range(num_of_digits):
        lst = [[] for i in range(num_of_digits)]
        for item in arr:
            num = item // 10 ** dgt % 10
            lst[num].append(item)
        arr = reduce( lambda x, y: x + y, lst)
    return arr
arr = [3,4,1,0,40,3333,32,2,5,3,45332]
print(radix_sort(arr))
