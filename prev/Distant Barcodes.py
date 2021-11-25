from typing import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes):
        if barcodes == []:
            return barcodes
        barcodes.sort()
        count = Counter(barcodes)
        arr = []
        for i in count:
            arr.append([count[i],i])
        arr = sorted(arr)[::-1]
        ind = 0
        for i in arr:
            for _ in range(i[0]):
                if ind >= len(barcodes):
                    ind = 1
                barcodes[ind] = i[1]
                # print(f'bar {barcodes} ind {ind} i {i}')
                ind +=2
        return barcodes





obj= Solution()
arr = [2,2,1,3]
print(obj.rearrangeBarcodes(arr))




