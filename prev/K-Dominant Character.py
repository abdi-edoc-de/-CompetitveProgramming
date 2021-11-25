def main():
    st = input()
    n = len(st)
    lastSen = {}
    windows = {}
    for i in range(n):
        c = st[i]
        
        if c in lastSen:
            curWin = i - lastSen[c]
            windows[c] = max(curWin,windows[c])
        else:
            windows[c] = i+1
        lastSen[c] = i
    for i in lastSen:
        c = lastSen[i]
        windows[i] = max(windows[i],n-c)
    # minL = ''
    min = n
    for i in windows:
        if windows[i] < min:
            min = windows[i]
            # minL = i
    print(min)
main()

    
    