import math
def solve(n,k):
    hour = 0
    updatedComps = 1
    while updatedComps < n and updatedComps <= k:
        hour += 1
        updatedComps *= 2
    if (n-updatedComps) % k == 0:
        j = (n - updatedComps) //k
        print(hour+j)
        return
    else:
        j = (n - updatedComps) //k
        print(hour+j+1)
        return 
    
def main():
    t = int(input())
    for i in range(t):
        arr = list(map(int,input().split()))
        n = arr[0]
        k = arr[1]
        solve(n ,k)
main()