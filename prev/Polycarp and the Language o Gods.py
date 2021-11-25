def solve(st):
    ret = 0
    vs = 0
    for i in st:
        if i == 'v':
            vs +=1
        else:
            ret +=1
            ret += vs//2
            vs = 0    
    ret += vs//2
    print(ret)
def main():
    t = int(input())
    for i in range(t):
        solve(input())
main()