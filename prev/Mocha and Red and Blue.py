from os import altsep


def solve(n, s):
    opp_colors = {'R':'B','B':'R'}

    square = -1
    color = '-1'
    for i in range(n):
        if s[i] != '?':
            square = i
            color = s[i]
            break
    if square == -1:
        st = 'BR' * (n//2)
        st += ('B' * (n % 2))
        print(st)
        return
    ret = []
    if square % 2 == 0:
        colors = color + opp_colors[color]
        ret.append(colors * (square//2))
    else:
        colors = opp_colors[color] + color
        st = colors * (square //2)
        st += opp_colors[color]
        ret.append(st)
    ret.append(color)
    
    ind = 1
    for i in range(square+1,n):
        if s[i] == '?':
            ret.append(opp_colors[ret[ind]])
        
        else:
            ret.append(s[i])
        ind += 1
    
    print(''.join([j for j in ret]))


def main():
    t = int(input())
    for i in range(t):
        solve(int(input()),input())
main()
