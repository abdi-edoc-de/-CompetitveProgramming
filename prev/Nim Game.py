class Solution:
    def canWinNim(self, n: int) -> bool:
        res = set()
        dp = {}
        self.helper(res, False, n,dp)
        print(res)
        return True in res
    def helper(self, res, turn,n,dp):
        turn = not turn
        # if n in dp:
        #     res.add(dp[n])
        if n <= 3:
            res.add(turn)
        else:
            self.helper(res,turn,n-1,dp)
            self.helper(res, turn, n -2,dp)
            self.helper(res, turn, n-3,dp)
        dp[n] = turn
Solution().canWinNim(10)
st = '1'
while True:
    st += '1'
    if int(st) % (7 * 7) == 0:
        print(st)
        print(len(st))
        break