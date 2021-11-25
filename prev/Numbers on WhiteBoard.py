from typing import DefaultDict


def solve(n):
    if n==1:
        print(1)
        return
    nums = [i for i in range(1,n+1)]
    ret = []
    for i in range(n-1, -1,-1):
        if i != 0:
            res = nums[i] + nums[i-1]
            ret.append((nums[i],nums[i-1]))
            nums[i-1] = (res//2) + int(res%2!=0)
            
    print(2)
    for i in ret:
        print(i[0],i[1])
    







        

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        solve(n)
main()