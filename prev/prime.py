from math import ceil, sqrt
def main():
    n = int(input())
    if n -2 <= 2:
        print(-1)
        return
        
    isPrime = True
    num  = ceil(sqrt(n-2))
    
    for i in range(2,num + 1):
        if (n-2) % i == 0:
    
            isPrime = False
            break

    if isPrime:
        print(2, n-2)
        return
    print(-1)
k = set()
k.add((0,0))
print((0,1) in k)
main()