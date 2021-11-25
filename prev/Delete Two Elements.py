def solve(n , nums):
    summ = sum(nums)
    mean = summ/n
    ret = 0
    for i in range(len(nums)):
        if n!= 1 and (summ - nums[i]) / (n - 1) == mean:
            summ = summ - nums[i]
            n -= 1 
            # print(i)
            # break
            ret = i
    print(ret)
    # print(ret)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int,input().split())) 
        solve(n, nums)
main()