
def solve(n, bosses):
    count = 0
    count = bosses[0]
    bosses[0] =0
    for i in range(n):
        if i != 0 and bosses[i] != 0:
            bosses[i]+= bosses[i-1]
    l = 0
    for r in range(n):
        if bosses[r] == 0:
            l = r
        if bosses[r] - bosses[l] == 3:
            l = r
            count += 1   
    print(count)
    
            
        
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        bosses = list(map(int,input().split()))
        solve(n,bosses)
main()