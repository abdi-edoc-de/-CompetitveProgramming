import sys
def solve(s):
    arr = [[s[0],1]]
    n = len(s)
    for i in range(1,n):
        if s[i] == arr[-1][0]:
            arr[-1][1] +=1
        else:
            arr.append([s[i],1])
    res = sys.maxsize
    l = 0
    m = len(arr)
    for r in range(1,m):
        if arr[r][0] == arr[l][0]:
            l = r-1
        if r -l == 2:
            l +=1
            res = min(res,2+arr[r-1][1])
        if res == 3:
            print(res)
            return
    if res == sys.maxsize:
        print(0)
        return
    print(res)

def main():
    t = int(input())
    for _ in range(t):
        solve(input())
main()