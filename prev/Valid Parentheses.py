
class Solution:
    def isValid(self, s: str) -> bool:
        arr =[]
        first = "({["
        second = ")}]"
        for i in s:
            # print(arr[0])
            if i in first:
                arr.append(i)
            if i in second:
                print(arr[-1])
                if second.find(i) == first.find(arr[-1]):
                    arr.pop()
                else:
                    return False
        if arr == []:
            return True
        return False
obj = Solution()
print(obj.isValid("{[]}"))