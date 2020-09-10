from  ex5 import bai1
import math
class WellNetExp(bai1.StringExp):
    def __init__(self,exp):
        super().__init__(exp)

    def isWellNet(self):
        Ops = ['+','-','/','*']
        Number = ['1','2','3','4','5','6','7','8','9']
        stack = []
        for i in self.exp:
            if i == ' ':
                continue
            elif i in Number:
                continue
            if i == '(' or i in Ops:
                stack.append(i)
            else:
                if stack[0] != '(' :
                    return False
                if sum([i in Ops for i in stack]) > 1 :
                    return False
                while (stack[-1] != '(' and len(stack) > 0):
                    if stack[-1] not in Ops:
                        return False
                    stack.pop()
                stack.pop()
        if len(stack) == 0:
            return True
        return False


a = WellNetExp('(1+2)')
print(a.isWellNet())
