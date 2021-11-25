def main():
    n = list(map(int,input().split())) 
    k = n[1]
    arr = list(map(int,input().split())) 
    arr.sort()
    checkMap = {}
    pairMax = 0
    for i in arr:
        checkMap[i] = True

    for i in arr:
        # if i * k in checkMap and checkMap[i]:
        if checkMap[i]:
            pairMax +=1
            checkMap[i * k] = False

        
    print(pairMax)
main()        
