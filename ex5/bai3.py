from ex5 import bai1


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
def applyOp(b, a, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a // b

class NormalExp(bai1.StringExp):
    def __init__(self,exp):
        super().__init__(exp)
    def compute(self):
        list  = self.exp
        values = []
        ops =  []
        i = 0
        while i < len(list):
            if list[i] == ' ':
                i+=1
                continue
            elif list[i] == '(':
                ops.append(list[i])
            elif list[i].isdigit():
                # number = 0
                # while i<len(list) and list[i].isdigit() :
                #     number = number * 10 + int(list[i])
                #     i+=1
                values.append(int(list[i]))

            elif list[i] == ')':
                # print(values)
                # print(ops)
                while len(ops) != 0 and ops[-1] != '(':
                    a = applyOp(values.pop(),values.pop(),ops.pop())
                    values.append(a)

                ops.pop()
                # print(ops)
                # print(values)
            else:
                while (len(ops) != 0 and precedence(ops[-1]) >= precedence(list[i])):
                    values.append(applyOp(values.pop(),values.pop(), ops.pop()))
                ops.append(list[i])

            i += 1
        while len(ops) != 0:
            values.append(applyOp(values.pop(), values.pop(), ops.pop()))

        return values[-1]


a = NormalExp('( 2 + 3 )')
print(a.compute())





