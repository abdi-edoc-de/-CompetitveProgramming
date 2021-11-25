

# from typing import mappping


def main():
    n = int(input())
    arr = list(map(int,input().split()))    
    mapp = {}
    main_max = 1
    for i in arr:
        if i in mapp:
            mapp[i] +=1
            if mapp[i] > main_max:
                main_max = mapp[i]
        else:
            mapp[i] = 1
    sArr = list(set(arr))
    sArr.sort()
    dif = []
    for i in range(len(sArr)):
        if i < len(sArr) - 1:
            dif.append(sArr[i+1] - sArr[i])
    for i in range(len(dif)):
        k = 5
        temp = set()
        while i < len(dif) and k > 0 and k >= dif[i] :

            if dif[i] <= k:
                temp.add(sArr[i])
                temp.add(sArr[i+1])
                k -=dif[i]
            i +=1
        tempMax = 0
        for i in temp:
            tempMax += mapp[i]
        if main_max < tempMax:
            main_max = tempMax
    print(main_max)

main()
# n = 6 
# arr = [2,2,2,4,55]
# main(6,arr)
# print(arr[1:])