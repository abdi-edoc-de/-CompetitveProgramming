def main():
    n = int(input())
    nums = list(map(int,input().split()))
    nums.sort()
    negs = 0
    zeros = 0
    coins = 0
    for i in range(n):
        if nums[i] < 0:
            negs += 1
            coins += abs(-1 - nums[i])
        elif nums[i] == 0:
            zeros += 1
        else:
            coins += (nums[i]-1)
    if negs >= 0 and zeros > 0  :
        coins += zeros
    elif negs % 2 != 0 and zeros  <= 0:
        coins += 2
    print(coins)
        
main()