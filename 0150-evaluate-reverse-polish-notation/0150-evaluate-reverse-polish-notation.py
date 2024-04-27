class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number = []
        symbol = []
        a = 0
        for i in range(len(tokens)):
            if tokens[i].isalnum():
                number.append(tokens[i])
            elif len(tokens[i]) >1 and tokens[i][0] == "-" and(tokens[i][1:]).isalnum():
                number.append(int(tokens[i][1:])*-1)
            else:
                a = int(number.pop())
                b = int(number.pop())
                s = tokens[i]
                if s == "/":
                    number.append(ceil(b/a)if  b/a < 0 else b//a)
                elif s == "*":
                    number.append(b*a)
                elif s == "-":
                    number.append(b-a)
                else:
                    number.append(b+a)
        return int(number[-1])


        