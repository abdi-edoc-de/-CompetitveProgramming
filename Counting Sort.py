arr = [0, 2, 2, 1, 1, 0, 3]
max = arr[0]
for i in arr:
    if i > max:
        max=i
map={}
for i in range(max+1):
    map[i]=[]

for i in arr:
    if i in map:
        map[i].append(i)
    else:
        map[i]=[i]

    
arr=[]
print(map)
for i in map:
    arr +=map[i]
print(arr)


