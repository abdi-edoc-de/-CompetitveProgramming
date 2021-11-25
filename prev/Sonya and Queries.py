from typing import DefaultDict


map = DefaultDict(int)
def solve(st):
    
    if st[0] == '+':
        bin = numToBin(st[2:])
        bin = removeLeadingZeros(bin)
        map[bin] +=1
    elif st[0] == '-':
        bin = numToBin(st[2:])
        bin = removeLeadingZeros(bin)
        map[bin] -=1
    else:
        bin = removeLeadingZeros(st[2:])
        print (map[bin])

def main():
    n = int(input())
    for i in range(n):
        solve(input())
def numToBin(st):
    ret = []
    for i in st:
        if int(i) % 2 == 0:
            ret.append('0')
        else:
            ret.append('1')
    return ''.join(ret)
    
def removeLeadingZeros(st):
    for i in range(len(st)):
        if st[i] == '1':
            return st[i:]
    
    return '0'

main()