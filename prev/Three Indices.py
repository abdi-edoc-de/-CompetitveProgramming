def solve(n , nums):
    for i in range(n):
        nums[i] = [nums[i],-1,-1]
    min_val = (-1,-1)
    for i in range(n):
        if i == 0:
            min_val = (nums[i][0],i)
        else:
            if nums[i][0] < min_val[0]:
                min_val = (nums[i][0], i)
            if nums[i][0] > min_val[0]:
                nums[i][1] = min_val[1]
    min_val = (-1,-1)

    for i in range(n-1,-1, -1):
        if i == n-1:
            min_val = (nums[i][0], i)
        else:
            if nums[i][0] < min_val[0]:
                min_val = (nums[i][0],i)
            if nums[i][0] > min_val[0]:
                nums[i][2] = min_val[1]
        if nums[i][1] != -1 and nums[i][2] != -1:
            print('YES')
            print(nums[i][1]+1 , i+1, nums[i][2]+1)
            return

    
    print("NO")



def main(): 
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums  = list(map(int, input().split()))
        solve(n, nums)

main()