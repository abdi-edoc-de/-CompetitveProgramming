def solve(n):
    if int(n) % 2 == 0:
        print(0)
        return
    if int(n[0]) % 2 == 0:
        print(1)
        return
    for i in n:
        if int(i) % 2 == 0:
            print(2)
            return
    print(-1)
def main():
    t = int(input())
    for _  in range(t):
        solve(input())
main()
    
        