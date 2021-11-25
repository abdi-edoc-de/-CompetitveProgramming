def solve(n,m,k,shop):
    k.sort()
    k = k[::-1]
    mn = 0
    ind = 0
    for i in range(n):
        if k[i]-1 >= ind:
            mn += shop[ind]
            ind+=1
        else:
            mn += shop[k[i]-1]
    print(mn)
        


def main():
    t = int(input())
    for _ in range(t):
        n , m  = list(map(int,input().split()))
        k = list(map(int,input().split()))
        shop = list(map(int,input().split()))
        solve(n,m,k,shop)
main()