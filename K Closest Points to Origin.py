class Solution:
    def kClosest(self, points , k):
        arr = []
        for i in range(len(points)):
            arr.append([self.distance_from_origin(points[i]),i])
        arr=sorted(arr)
        arr1 = []
        for i in range(k):
            arr1.append(points[arr[i][1]])
        return arr1
        
        

    def distance_from_origin(self,arr):
        return (arr[0]**2  + arr[1]**2)**0.5
    
        

obj = Solution()
# print(obj.distance_from_origin([1,3]))
print(obj.kClosest([[-5,4],[-6,-5],[4,6]],2))

  