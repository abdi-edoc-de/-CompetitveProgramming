def main():
    n = int(input())
    if n == 1 or n == 2:
        print(-1)
    else:
        arr = [x for x in range(n,0,-1)]
        print(*arr)
main()
