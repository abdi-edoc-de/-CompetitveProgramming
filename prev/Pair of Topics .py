def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    mn = b[0]
    ma = a[0]
    for i in range(1,n):
        if a[i] + ma > b[i] + mn:
            count += 1
        ma = max(ma, a[i])
        mn = min(mn,a[i])
    print(count)
main()