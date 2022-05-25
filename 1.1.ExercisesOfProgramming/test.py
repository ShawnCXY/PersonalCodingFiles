# coding:utf-8
# 全站排名 86,668


class Solution:
    def countEval(self, s: str, result: int) -> int:
        def backTrace(s, res):
            if len(s) == 1:
                if int(s[0]) == result:
                    res[0] += 1
            else:
                for i in range(0,len(s)-2,2):
                    v = '0'
                    if s[i+1] == '|' and (s[i] == '1' or s[i+2] == '1'):
                        v = '1'
                    if s[i+1] == '&' and s[i] == '1' and s[i+2] == '1':
                        v = '1'
                    if s[i+1] == '^' and s[i] != s[i+2]:
                        v = '1'
                    backTrace(s[:i]+[v]+s[i+3:], res)
        res = [0]
        backTrace(list(s), res)
        return res[0]

solo = Solution()
print(solo.countEval("0&0&0&1^1|0",1))


