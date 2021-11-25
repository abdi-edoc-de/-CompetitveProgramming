def solve(n, ct, moment):
    prev = 0
    ind = 0
    length = len(moment)
    for i in range(n):
        duration = prev + ct[i][0] * ct[i][1]
        prev = duration
        while True:
            if ind == length:
                break
            if moment[ind] <= duration:
                print(i+1)
                ind+=1
            else:
                break
        
def main():
    arr = list(map(int,input().split()))
    
    ct = []
    for i in range(arr[0]):
        ct.append(list(map(int,input().split())))
    moment = list(map(int,input().split()))
    solve(arr[0], ct, moment)
main()
