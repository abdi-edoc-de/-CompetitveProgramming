class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix = [height[0]]
        for i , item in enumerate(height[1:], start = 1):
            prefix.append(prefix[i-1] + item)
        stack = [[height[0], 0, 0]]
        res = 0
        flag = False
        for i, item in enumerate(height[1:], start = 1):
            while stack and stack[-1][0] <= item:
                h , prev, ind = stack.pop()
                res -= prev
            
            if stack :
                top =  stack[-1][2]
                cur = (((item * (i - top - 1)) ) - (prefix[i-1] - prefix[top]) )
                
                res += cur - stack[-1][1]
                stack[-1][1] = cur
                
                # print(res,cur,item,stack)
            else:
                res += (((h * (i - ind - 1)) ) - (prefix[i-1] - prefix[ind]))
            stack.append([item,0,i])
        return res     
        