class StringExp:
    def __init__(self,exp):
        self.exp = exp

    def isValid(self):
        openlist = ['(','[','{']
        closelist = [')','[','}']
        stack = []
        if all([i in openlist for i in self.exp]) :
            return "Not Balanced"
        if all([i in closelist for i in self.exp]):
            return "Not Balanced"
        for i in self.exp:
            if i in openlist:
                stack.append(i)
            elif i in closelist:
                check = closelist.index(i)
                if((len(stack) > 0) and (openlist[check] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return "Not Balanced"
        if len(stack) == 0 :
            return "Balanced"

a = StringExp('(1+2)')
print(a.isValid())