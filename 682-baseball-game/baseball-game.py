class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                # Pichle do scores ko add karke push karein
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Pichle score ka double karke push karein
                stack.append(2 * stack[-1])
            elif op == "C":
                # Pichle score ko remove karein
                stack.pop()
            else:
                # Agar number hai to integer mein convert karke push karein
                stack.append(int(op))        
        # Sabhi valid scores ka total sum return karein
        return sum(stack)
