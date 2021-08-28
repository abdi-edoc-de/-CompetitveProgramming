class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) :
        arr = []
        for y in range(rows):
            for x in range(cols):
                d = abs(y-rCenter) +abs(x-cCenter)
                arr.append([d,y,x])
        arr = sorted(arr)
        for i in range(len(arr)):
            arr[i]=arr[i][1:3]
        return arr


obj = Solution()
print(obj.allCellsDistOrder(2,3,1,2))


