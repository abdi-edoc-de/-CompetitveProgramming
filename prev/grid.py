def grid_path(m,n):
    if m ==1 or n== 1:
        return 1
    else:
        return grid_path(m-1,n) + grid_path(m,n-1)
def partion(n,m):
    if m>=n:
        return 1
    else:
        return partion(n,m) + partion(n-m,m)
    
    
    
print(partion(6,3))

