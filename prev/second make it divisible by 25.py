def divisibleBy25(n):
    n = str(int(n))
    size = len(n)
    steps = size

    for i in range(size):
        for k in range(i+1,size):
            st = n[i]+n[k]
            if st in ['00','25','50','75']:
                steps = min(steps,size-(i+gb))

    print(steps)
    
        
def main():
    t = int(input())
    for i in range(t):
        divisibleBy25(input())

        
main()