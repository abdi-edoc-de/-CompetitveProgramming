


from collections import deque
# from typing import Deque


def solve(ans, arr,check):
    n = len(arr)
    if n == 0:
        print(*ans)
        return
    if n == 1:
        ans = ans + arr
        print(*ans)
        return
    
    que = deque(arr)
    que2 = deque(ans)
    while len(que) > 2:
        if que[0] == min(que[0], que[-1]):
            que2.appendleft(que.popleft())
        else:
            que2.append(que.pop())
    que2.append(que.pop())
    que2.appendleft(que.popleft())
    que = deque()
    last = list(que2)


    while len(que2) > 1:
        if que2[0] == min(que2[0], que2[-1]):
            que.appendleft(que2.popleft())
        else:
            que.append(que2.pop())
    que.append(que2.pop())
   
    if que[0] == max(que[0], que[-1]):
        que.popleft()
    else:
        que.pop()
    check = list(que)

    if arr == check:
        print(* last)
    else:
        print(-1)

def main():
    t = int(input())
    for _ in range(t):
        n = input()
        arr = list(map(int,input().split()))
        ma = max(arr[0],arr[-1])
        ans = [ma]
        check = arr.copy()
        if ma == arr[0]:
            arr = arr[1:]
        else:
            arr.pop()
        solve(ans,arr,check)
main()