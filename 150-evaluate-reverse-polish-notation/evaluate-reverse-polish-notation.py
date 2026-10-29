class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack  = []
        for token in tokens:
            if token not in {"+","-","*","/"}:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b) #impotant hai yaad rakhna hai 
                stack.append(result)
        return stack[-1]


        