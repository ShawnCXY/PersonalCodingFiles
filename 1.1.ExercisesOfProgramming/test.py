# coding:utf-8


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        digits, operate = [], []
        lenS = len(s)
        i = 0
        while i < lenS:
            print("i:{}, s[i]:{}, digits:{}, ope:{}".format(i, s[i], digits, operate))
            if s[i] in '0123456789':
                j = i
                while j < lenS and s[j] in '0123456789':
                    j += 1
                digits.append(int(s[i:j]))
                i = j
            else:
                if len(operate) == 0:
                    operate.append(s[i])
                    i += 1
                elif s[i] in '+-' and operate[-1] in '+-':
                    while len(operate)>0 and s[i] in '+-' and operate[-1] in '+-':
                        right, left = digits.pop(), digits.pop()
                        oper = operate.pop()
                        if oper == '+':     
                            digits.append(left+right)
                        else:
                            digits.append(left-right)
                    operate.append(s[i])
                    i += 1
                elif s[i] in '+-' and operate[-1] in '*/':
                    while len(operate) > 0 and s[i] in '+-' and operate[-1] in '*/':
                        right, left = digits.pop(), digits.pop()
                        oper = operate.pop()
                        if oper == '*':     
                            digits.append(left*right)
                        else:
                            digits.append(left//right)
                    operate.append(s[i])
                    i += 1
                elif s[i] in '*/' and operate[-1] in '+-':
                    operate.append(s[i])
                    i += 1
                else:
                    while len(operate) > 0 and s[i] in '*/' and operate[-1] in '*/':
                        right, left = digits.pop(), digits.pop()
                        oper = operate.pop()
                        if oper == '*':     
                            digits.append(left*right)
                        else:
                            digits.append(left//right)
                    operate.append(s[i])
                    i += 1
            print("digits:{}, ope:{}".format(digits, operate))
        while len(operate) > 0:
            right, left = digits.pop(), digits.pop()
            oper = operate.pop()
            if oper == '*':     
                digits.append(left*right)
            elif oper == '/':
                digits.append(left//right)
            elif oper == '+':
                digits.append(left+right)
            else:
                digits.append(left-right)
        return digits[0]


solo = Solution()
solo.calculate("3+2*2")


