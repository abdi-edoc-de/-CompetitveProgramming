def main():
    n = int(input())
    stairs = list(map(int,input().split()))
    m = int(input())
    boxs = []
    for i in range(m):
        boxs.append(list(map(int,input().split())))
    max_h = stairs[0]
    for i in range(m):
        h = boxs[i][1]
        w = boxs[i][0] - 1
        if stairs[w] >= max_h:
            print(stairs[w])
            max_h = stairs[w] + h
        else:
            print(max_h)
            max_h += h
main()
    

