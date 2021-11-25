class Solution:
    def sortColors(self, nums):

        arr = nums
        max = arr[0]
        for i in arr:
            if i > max:
                max=i
        arr2=[]
        for i in range(max+1):
            arr2.append(0)

        for i in arr:
            arr2[i]+=1
        arr=[]
        k = 0
        for i in range(len(arr2)):
            for j in range(arr2[i]):
                arr.append(i)
                k+=1
        print(k)
        print(arr)

obj = Solution()
print(obj.sortColors([2,1,2,0,2,1,0]))