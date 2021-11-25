# from math import abs
def solve(start,dest):

    rook(start, dest)
    bishop(start, dest)
    king(start, dest)
def bishop(start,dest):
    isOdd = (start[0] + start[1])%2 == 0  and\
         (dest[0] + dest[1])%2 == 0
    isEven = (start[0] + start[1])%2 != 0 and\
         (dest[0] + dest[1])%2 != 0
    if isOdd or isEven:
        if abs(start[0] - dest[0]) == abs(start[1]- dest[1]):
            print(1)
        else:
            print(2)
    else:
        print(0)
def rook(start,dest):
    
    if start[0] == dest[0]:
        print(1)
    elif start[1] == dest[1]:
        print(1)
    else:
        print(2)
def king(start,dest):

    if abs(start[0] - dest[0]) == abs(start[1]- dest[1]):
        print(abs(start[0] - dest[0]))
    else:
        x = abs(start[0] - dest[0])
        y = abs(start[1] - dest[1]) 
        print(min(x, y)+ abs(x -y))
def main():
    inp =list(map(int,input().split())) 
    solve([inp[1],inp[0]],[inp[3],inp[2]])


main()

