class Solution:
    def minTimeToType(self, word):
        sec = 0
        for i in range(len(word)):
            if i == 0:
                clockWise = ord(word[i]) - ord('a')
                counter = ord('z') - ord(word[i]) + 1

            else:
                if ord(word[i-1]) > ord(word[i]):
                    counter = ord(word[i]) - ord(word[i-1])
                    clockWise = ord('z') - ord(word[i-1]) + ord(word[i]) - ord('a') + 1
                elif ord(word[i-1]) < ord(word[i]):
                    clockWise = ord(word[i]) - ord(word[i-1])
                    counter = ord('z') - ord(word[i]) + ord(word[i-1]) - ord('a') + 1
                else:
                    counter = 0
                    counter = 0
            mov = 0
            counter = abs(counter)
            clockWise = abs(clockWise)
            if counter < clockWise:
                mov = counter
            else:
                mov = clockWise
            
            sec = sec + mov + 1
        return sec
obj = Solution()
word = "zjpc"
print(obj.minTimeToType(word))
                

                # clockWise =  - 
                # j = 2



# print(ord('z') - ord('a')+1)
# print(ord('e') - ord('b'))
# print(ord('z') - ord("b") + ord('e') - ord('a') + 1)
# print(ord('z') - ord('y'))
# print( ord('a')-ord('a') +1)
        