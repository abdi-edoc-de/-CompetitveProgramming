def solve(n,k,mice):
    mice.sort()
    catsStep = 0
    count = 0
    for i in range(k - 1,-1,-1):
        step = n- mice[i]
        if catsStep < mice[i]:
            catsStep += step
            count+=1
    print(count)
        

def main():
    t = int(input())
    for _ in range(t):
        n ,k = list(map(int,input().split()))
        mice = list(map(int, input().split()))
        solve(n,k,mice)
main()