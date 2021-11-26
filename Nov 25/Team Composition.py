def solve(a, b):
    if a == b:
        print(a//2)
        return
    if a < 1 or b < 1 or a + b < 4:
        print(0)
        return
    
    ans = 0
    dif = abs(a - b)
    ma = max(a, b)
    mn = min(a , b)
    num = (dif // 3 ) 
    if mn <= num:
        print(mn)
        return
    mn -= num
    ans += num
    ma -= (num * 3)

    if mn + ma < 4 or ma == 0:
        print(ans)
        return
    ans += mn // 2
    print(ans)

    
    

    
    
def main():
    t = int(input())
    for _ in range(t):
        a, b = list(map(int,input().split()))
        solve(a,b)
main()