from typing import NamedTuple


class Solution:
    def getFolderNames(self, names):
        map = {}

        for i in range(len(names)-1):
            if names[i] in map:
                map[names[i]][0] +=1
            else:
                map[names[i]] = [0,i,0]
        for i in map:


        