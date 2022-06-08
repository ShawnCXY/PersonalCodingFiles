# coding:utf-8
# 全站排名 86,668
# 全站排名 86,330
# 全站排名 85,288



class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        if k is None or k <= 0:
            return None
        resList = [1]
        i, j, k = 0, 0, 0
        for _ in range(k-1):
            v = min(resList[i]*3, resList[j]*5, resList[k]*7)
            resList.append(v)
            if v % 3 == 0:
                i += 1
            if v % 5 == 0:
                j += 1
            if v % 7 == 0:
                k += 1
        return resList[-1]

solo = Solution()
print(solo.getKthMagicNumber(10))


