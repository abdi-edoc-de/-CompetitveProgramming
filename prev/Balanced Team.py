def main():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ret = []
    he = []
    for i in range(len(arr)):
        if len(he) == 0:
            he.append(arr[i])
        elif len(he) > 0:
            if arr[i] - he[-1] > 5:
                he = [arr[i]]
            elif arr[i] - he[-1] <= 5 and arr[i] - he[0] <= 5:
                he.append(arr[i])
            else:
                while len(he)> 0 and arr[i] - he[0] > 5:
                    he = he[1:]
                he.append(arr[i])

        ret.append(len(he))    
    print(max(ret))
main()
# n = 6 
# arr = [2,44,67]
# main(6,arr)
# print(arr[1:])