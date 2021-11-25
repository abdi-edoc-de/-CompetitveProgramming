from typing import Counter


class TopVotedCandidate:
    
    def __init__(self, persons, times):
        self.times= times
        self.persons= persons

    def q(self, t: int) -> int:
        l = 0
        r = len(self.times) - 1
        index = -1
        while l <= r:
            mid = l + (r - l)//2
            if self.times[mid] <= t:
                index = mid
                l = mid + 1
            else:
                r = mid - 1
        persons = self.persons[:index+1]
        print(persons)
        count = Counter(persons)
        most_c = Counter.most_common(count)
        print(Counter.most_common(count))
        max = most_c[0][1]
        arr =[]
        for i in most_c:
            if i[1] < max :
                break
            else:
                arr.append(i)
        if len(arr) == 1:
            return arr[0][1]
        # for i in range(len(persons)-1,-1,-1):
            
        # print(arr)
            
                   

persons = [0, 1, 1, 0, 1,0, 0]
times = [0, 5, 10, 15, 20, 25, 30]
obj = TopVotedCandidate(persons , times)
print(obj.q(24))
        
        
