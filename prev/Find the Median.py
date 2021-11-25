
def findMedian(arr):
    # Write your code here
    arr= sorted(arr)
    if len(arr) > 0:
        return arr[int(len(arr)/2)]
    return 0

print(findMedian([]))
