from typing import Counter


class Solution:
    def reorganizeString(self, s):
        arr_string = list(s)

        if arr_string == []:
            return arr_string
        arr_string.sort()
        count = Counter(arr_string)
        arr = []
        for i in count:
            arr.append([count[i],i])
        arr = sorted(arr)[::-1]
        ind = 0
        for i in arr:
            for _ in range(i[0]):
                if ind >= len(arr_string):
                    ind = 1
                arr_string[ind] = i[1]
                # print(f'bar {arr_string} ind {ind} i {i}')
                ind +=2
        for i in range(len(arr_string)-2):
            if arr_string[i] == arr_string[i+1]:
                return ""
        return "".join([str(i) for i in arr_string])

obj = Solution()
arr = 'aababcab'
print(obj.reorganizeString(arr))