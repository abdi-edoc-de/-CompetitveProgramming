class Solution:
    def pancakeSort(self, arr):
        orderInd = len(arr)
        k_arr =[]
        
        while orderInd != 0:
            # print(arr)
            if arr == sorted(arr):
                # print(f'this the k values {k_arr}')
                return k_arr
            max_num =  max(arr[0:orderInd])
            index_max_num = arr.index(max_num)
            k_arr.append(index_max_num+1)
            arr = arr[:index_max_num+1][::-1] + arr[index_max_num+1:len(arr)]
            arr = arr[:orderInd][::-1]+arr[orderInd:len(arr)]
            k_arr.append(orderInd)
            orderInd -=1
        # print(f'this the k values {k_arr}')
        # return k_arr
        return k_arr

obj = Solution()
arr=[1,2,3,4]
print(f'this is the last {obj.pancakeSort(arr)}')


# arr =[1,2,3]
# max = arr.index(3)
# print(arr[:3+1][::-1] + arr[3+1:3])
# print(arr[4:3])