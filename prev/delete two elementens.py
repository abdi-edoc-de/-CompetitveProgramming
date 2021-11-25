from collections import defaultdict
from typing import MutableMapping


def solve(n, nums):
    summ = sum(nums)
    mean = summ/n

    numsN = {}
    val = 0
    for i in range(n):
        x = (summ - nums[i]) - (mean * (n -2))
        if x in numsN:
            val += numsN[x]
        if nums[i] in numsN:
            numsN[nums[i]] += 1
        else:
            numsN[nums[i]] = 1
    print(val)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int,input().split())) 
        solve(n , nums)
main()