class Solution:
    def relativeSortArray(self, arr1,arr2):
        map={}
        for i in arr2:
            map[i]=[]

        not_in_arr2 = []
        for i in arr1:
            if i in map:
                map[i].append(i)
            else:
                not_in_arr2.append(i)
            
        not_in_arr2 = sorted(not_in_arr2)
        arr=[]
        for i in map:
            arr += map[i]
    
        return arr + not_in_arr2

arr1 = [28,6,22,8,44,17]
arr2 =  [22,28,8,6]
obj = Solution()
print(obj.relativeSortArray(arr1,arr2))




        