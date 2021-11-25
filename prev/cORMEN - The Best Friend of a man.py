def solve(n,k, affairs):

    mn =0
    for i in range(1,n):
        count =k-( affairs[i-1] + affairs[i])
        count = max(0,count)
        mn += count
        affairs[i] += count
    print(mn)
    print(*affairs)


def main():
    n,k = list(map(int,input().split()))
    affairs = list(map(int,input().split()))
    solve(n, k, affairs)
main()
