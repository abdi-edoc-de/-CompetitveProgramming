arr = [[1,2,3],[4,5,6],[7,8,9]]
a = arr[0:2]
m= 3
n = 3

ret = [[0] * n] * m
print(ret)
for i in range(len(a)):
    a[i] = a[i][0:2]
print(a)
def prefixSum(arr):
    sum = 0

    for i in arr:
        for j in i:
            sum +=j
    return sum
print(prefixSum(a))
import math

print(math.log2(6))
print(arr[2])
# s = [1,2,3,5]
# s.add(5)
# s.add(4)
# s.add(3)
j = [[1,2],[2,3]]
j[0] = j[1]
j[0][0] = 44
print(j)
# print(s.pop())

x = input().split()