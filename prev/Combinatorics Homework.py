def solve(a,b,c,m):
    max_val = a + b + c - 3
    val = [a,b,c]
    val.sort()
    min= val[2] - val[0] - val[1]-1
    if min <= m <= max_val:
        print('YES') 
        return
    print('NO') 
# print(len(ma))   
def main():
    t = int(input())
    for i in range(t):
        arr = list(map(int,input().split()))
        solve(arr[0],arr[1],arr[2],arr[3])
    
main()
