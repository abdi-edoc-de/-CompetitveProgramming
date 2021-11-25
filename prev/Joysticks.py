def main():
    a, b = list(map(int,input().split()))
    count  =0 
    while (a > 0 and b > 0) : 
        if a < 2 and b < 2:
            break
        count+=1
        a,b = min(a,b),max(a,b)
        a +=1
        b -=2   
    print(count)

main()