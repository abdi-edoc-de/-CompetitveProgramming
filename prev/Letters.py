def main():
    n,m = list(map(int,input().split()))
    dorms = list(map(int,input().split()))
    postas = list(map(int,input().split()))
    
    for i in range(n):
        if i != 0:
            dorms[i] += dorms[i-1]
    
    ind = 0
    for i in postas:
        while dorms[ind] < i:
            ind+=1
        if ind == 0:
            print(ind+1,i)
        else:
            print(ind+1,i-dorms[ind-1])
main()