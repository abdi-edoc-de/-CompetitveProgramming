def main():
    startValue , target = list(map(int,input().split()))
    
    steps = 0
    
    while target > startValue:
        if target % 2 == 0:
            target = target/2
            steps +=1
        else:
            target += 1
            target /= 2
            steps += 2
    print( int((startValue - target) + steps))          
main()