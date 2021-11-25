class Solution:
    def countPaths(self, n: int, roads) -> int:
        stack = []
        map = {}
        for i in roads:
            if i[0] in map:
                map[i[0]].append([i[1],i[2]])
            else:
                map[i[0]] = [[i[1],i[2]]]
            # if i[1] in map:
            #     map[i[1]].append([i[0],i[2]])
            # else:
            #     map[i[1]] = [[i[0],i[2]]]
        print(map)
       


        # print(map)
obj = Solution()

roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(obj.countPaths(7,roads))      