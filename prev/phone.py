class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        digitToLetters = {}
        
        letter = ord('a')
        
        for i in range(2,10):
            if i == 9 or i == 7:
                limit = 4
            else:
                limit = 3
            for char in range(limit):
                if i in digitToLetters:
                    digitToLetters[i].append(chr(letter))
                else:
                    digitToLetters[i] = [chr(letter)]
                letter += 1
        ret = digitToLetters[int(digits[0])]
        
        for i in range(1,n):
            temp = []
            for char in digitToLetters[int(digits[i])]:
                for cur in ret:
                    temp.append(cur + char)
            ret = temp
        # print(digitToLetters)
        return ret
        
        
