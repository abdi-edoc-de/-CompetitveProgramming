arr =  [0, 2, 2, 1, 1, 0, -5, 3]

i=0
while i<len(arr):
    index= i
    j= i-1
    t=True
    while j>=0 :
        if arr[j] > arr[index]:
            arr[j],arr[index]=arr[index],arr[j]
            index=j;
        j-=1      
    i+=1
print(arr)
