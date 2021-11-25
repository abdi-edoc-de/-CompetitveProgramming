def main():
    n = int(input())
    nums = list(map(int,input().split()))
    l= 0
    best = 1
    for r in range(n):
        if r != 0 and nums[r-1] >= nums[r]:
            l = r
        best = max(best,r-l+1)
    print(best)
main() 