

def main():
    yW =  list(map(int,input().split())) 
    val = max(yW)
    dotVal = 7 - val
    neum = dotVal
    demo = 6
    for i in range(1,7):
        if neum % i == 0 and demo % i == 0:
            neum = neum / i
            demo = demo/ i
    print(f'{int(neum)}/{int(demo)}')
main()