def solve(n, arr):
    if arr[0] == 0:
        st = 'a'
        s = ['a','ba']
    else:
        st = 'a' * arr[0]
    
        s = [st,st]
    last = ord('z')
    for i in range(1,n):
        st = s[-1]
        if arr[i] == 0:
            st = s[-1]
            char = ord(st[0]) + 1
            if char > last:
                st = 'a' + st
            else:
                st = chr(char) + st
            s.append(st)
        elif arr[i] <= arr[i-1]:
            s.append(st[:arr[i]])
        else:
            st = s[-1]
            s.pop()
            st = st[0] * arr[i]
            s.append(st)
            s.append(st)
    for i in s:
        print(i)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        solve(n,arr)
main()