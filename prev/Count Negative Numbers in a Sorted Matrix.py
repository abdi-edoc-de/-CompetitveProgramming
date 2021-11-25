class Solution:
    def countNegatives(self, grid) -> int:
        count = 0
        for i in grid:
            l = 0 
            r = row_size = len(i) -1
            countInRow = 0
            while (l <= r):
                mid = l + (r - l)//2
                # if grid[0] == i:
                #     print(f'count {countInRow}')
                #     print(mid)
                #     print(row_size)
                if i[mid] < 0:
                    countInRow = row_size - mid +1
                    r = mid -1
                else:
                    l = mid + 1
            
            print(countInRow)
            count +=countInRow
        return count
obj = Solution()
arr =  [[8,-2,-2,-2,-4,-5,-5],
[-2,-3,-3,-4,-4,-5,-5],
[-2,-5,-5,-5,-5,-5,-5],
[-3,-5,-5,-5,-5,-5,-5],
[-5,-5,-5,-5,-5,-5,-5],
[-5,-5,-5,-5,-5,-5,-5],
[-5,-5,-5,-5,-5,-5,-5],
[-5,-5,-5,-5,-5,-5,-5],
[-5,-5,-5,-5,-5,-5,-5]]
# arr = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# arr = [[8,-2,-2,-2,-4,-5,-5]]
print(obj.countNegatives(arr))
