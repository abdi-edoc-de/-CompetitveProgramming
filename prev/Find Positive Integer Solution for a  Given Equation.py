class Solution:
    def findSolution(self, customfunction, z) :
        ret = []
        for i in range(1,1001):
            l = 1
            r = 1000
            while l <= r:
                mid = l + (r - l)//2

                if customfunction.f(i,mid) == z:
                    ret.append([i,mid])
                    break
                elif customfunction.f(i,mid) < z:
                    l = mid+1
                else:
                    r = mid - 1
        return ret


            



        