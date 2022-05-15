# coding:utf-8
# 全站排名 86,668


class Solution:
    def solveNQueens(self, n: int):
        def backTrace(r, path, diag1, diag2):
            if r == n:
                tRes = []
                for c in path:
                    temp = ""
                    for v in range(n):
                        if v == c:
                            temp+='Q'
                        else:
                            temp+='.'
                    tRes.append(temp)
                res.append(tRes)    
            else:
                for c in range(n):
                    # 不同行列/不同对角线
                    if c in path or r+c in diag1 or r-c in diag2:
                        continue
                    path.append(c)
                    diag1.add(r+c)
                    diag2.add(r-c)
                    backTrace(r+1, path, diag1, diag2)
                    diag1.remove(r+c)
                    diag2.remove(r-c)
                    path.pop()
        res = []
        if n is None or n <= 0:
            return [[]]
        backTrace(0, [], set(), set())
        return res

solo = Solution()

print(solo.solveNQueens(4))


