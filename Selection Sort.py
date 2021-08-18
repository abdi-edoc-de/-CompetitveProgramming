arr = [0, 2, 2, 1,-10, 1, 0, -5, 3]

i=0
while i<len(arr):
    min= arr[i];
    minIndex = i;
    j=i;
    while j<len(arr):
        if arr[j]<min:
            min =arr[j];
            minIndex = j;
        j+=1;
    arr[i],arr[minIndex]=arr[minIndex],arr[i]
    i+=1

print(arr)
    
    