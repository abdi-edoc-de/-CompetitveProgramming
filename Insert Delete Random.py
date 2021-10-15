class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.set = []
        
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = val
        self.set.append(val)
        return True   
        

    def remove(self, val: int) -> bool:
        if val in self.map:
            del self.map[val]
            self.set.remove(val)
            return True
        return False
        

    def getRandom(self) -> int: 
        siz = len(self.set)
        ind = random.randint(0,siz-1)
        return self.set[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
