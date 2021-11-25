def solve(n, arr):

    for i in range(n-1, -1, -1):
        ind = i + arr[i]
        if ind < n:
            arr[i] += arr[ind]
    print(max(arr))

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        solve(n, arr)
main()
