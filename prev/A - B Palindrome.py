from typing import Counter
def solve(a,b,s):
    n = len(s)
    if a % 2 != 0 and b % 2 !=0:
        print(-1)
        return
    count =Counter(s)
    for i in range(n):
        # print(s,s[i],s[n-i-1])
        if i == (n - i - 1) and s[i] == '?':
            if a- count['0'] >= 1:
                s[i] = '0'
                count['0'] += 1
            elif b - count['1'] >= 1:
                count['1'] += 1
                s[i] = '1'
            else:
                print(-1)
                return
        elif s[i] != '?' and s[n-i -1] != '?' and s[i] != s[n-i -1]:
            print(-1)
            return
        elif s[i] == '?' and s[n-i-1] == '?':
            if a - count['0']  >= 2:
                count['0'] += 2
                s[i] = '0'
                s[n-i-1] = '0'
            elif b- count['1']  >= 2:
                count['1'] += 2
                s[i] = '1'
                s[n-i-1] = '1'
            else:
                print(-1)
                return
        elif s[i] == '?':
            if s[n-i-1] == '0':
                if a - count['0']  >= 1:
                    count['0'] += 1
                    s[i] = '0'
                else:
                    print(-1)
                    return
            elif s[n - i -1] == '1':
                if b-count['1'] >= 1:
                    count['1'] += 1
                    s[i] = '1'
                else:
                    print(-1)
                    return
        elif s[n-i-1] == '?':
            if s[i] == '0':
                if a-count['0'] >= 1:
                    count['0'] += 1
                    s[n-i-1] = '0'
                else:
                    print(-1)
                    return
            elif s[i] == '1':
                if b-count['1'] >= 1:
                    count['1'] += 1
                    s[n-i-1] = '1'
                else:
                    print(-1)
                    return
    count = Counter(s)
    print(count)
    if count['0'] != a:
        print(-1)
        return
    if count['1'] != b:
        print(-1)
        return
    print(''.join(s))

def main():
    t = int(input())
    for _ in range(t):
        a,b = list(map(int,input().split()))
        s = input()
        solve(a,b,[x for x in s])
main()