

from collections import defaultdict


def solve(n, red, blue):
    # red = removeZeros(red)
    # blue = removeZeros(blue)

    redVal = 0
    blueVal = 0
    for i in range(n):
        if int(red[i]) < int(blue[i]):
            blueVal += 1
        if int(red[i]) > int(blue[i]):
            redVal += 1
    if redVal > blueVal:
        print('RED')
    elif redVal < blueVal:
        print('BLUE')
    else:
        print('EQUAL')

def removeZeros(st):
    for i in range(len(st)):
        if st[i] != '0':
            return st[i:]
    return '0'
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        red = input()
        blue = input()
        solve(n, red, blue)
main()