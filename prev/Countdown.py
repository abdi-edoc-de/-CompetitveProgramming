
def solve(n , s):
    count = 0
    for i in range(n):
        if i != n -1 and s[i] != '0':
            count+=1
        count+= int(s[i])
    print(count)
    

def main():
    t = int(input())
    for i in range(t):
        solve(int(input()), input())
main()