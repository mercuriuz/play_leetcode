class Solution:
    def isValid(self, s: str) -> bool:
        def match(c1, c2):
            if c1 == '{' and c2 == '}':
                return True
            if c1 == '[' and c2 == ']':
                return True
            if c1 == '(' and c2 == ')':
                return True
            return False
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                pop = stack[-1]
                if match(pop, c):
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0