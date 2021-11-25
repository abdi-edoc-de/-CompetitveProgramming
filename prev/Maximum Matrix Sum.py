class Solution:
    def maxMatrixSum(self, matrix) -> int:
        min = abs(matrix[0][0])
        negNum = 0
        sum = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                sum += abs(matrix[row][col])
                if matrix[row][col] < 0:
                    negNum +=1
                if abs(matrix[row][col]) < min:
                    min = abs(matrix[row][col])
        print(sum)
        if negNum % 2 == 0:
            return sum
        return sum - 2 * abs(min)

arr = [[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]
obj = Solution()
print(obj.maxMatrixSum(arr))