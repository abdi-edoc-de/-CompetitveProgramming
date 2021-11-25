class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        arr = []
        stack = []
        for i in range(len(temperatures)):
            cur = [i , temperatures[i]]
            while stack != [] and cur[1]>stack[-1][1]:
                prev = stack.pop()
                ans[prev[0]] = cur[0] - prev[0]
            stack.append(cur)
        return ans

        

        
# obj = Solution()
# a = [73,74,75,71,69,72,76,73]
# print(obj.dailyTemperatures(a))
# print(eval('(3+3)/2'))
# print(len(arr))
# print(arr[len(arr)])
# arr = []
# for i in range(200):
#     temp = []
#     for j in range(200):
#         temp.append(0)
#     arr.append(temp)
# for i in range(len(arr)):
#     for j in range(len())
# print(arr)
arr = [1,2,3]
print(arr[-3])