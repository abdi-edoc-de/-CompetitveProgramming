class RecentCounter:
    
    def __init__(self):
        self.pings = []
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        ret = 0
        for i in self.pings:
            if t-3000 <= i <= t:
                ret+=1
        return ret


obj = RecentCounter()

print(obj.ping(5))
# print(obj.ping(6))
print(obj.ping(1))
print(obj.ping(3002))
print(999978490<=10**9)