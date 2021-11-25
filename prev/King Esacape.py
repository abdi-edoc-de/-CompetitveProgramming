def solve(n, queen , king, dest):
    # print(queen)
    # print(king)
    # print(dest)
    kingsCord = getCordant(n, queen, king)
    destCord = getCordant(n, queen,dest, )
    # print(kingsCord)
    # print(destCord)
    if kingsCord == destCord:
        print('YES')
    else:
        print('NO')
def getCordant(n,queen, spot):

    if 0<  spot[0] < queen[0] and 0 < spot[1] < queen[1]:
        return '3'
    elif queen[0] < spot[0] <= n and 0 < spot[1] < queen[1]:
        return '4'
    elif 0 < spot[0] < queen[0] and queen[1] < spot[1] <= n:
        return '1'
    elif queen[0] < spot[0] <= n and queen[1] < spot[1] <= n:
        return '2'  






def main():
    n = int(input())
    queen = list(map(int,input().split())) 
    king = list(map(int,input().split())) 
    dest = list(map(int,input().split())) 
    solve(n, queen, king,dest)
main()