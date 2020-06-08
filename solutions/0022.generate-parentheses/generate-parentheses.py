class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def back(combination, left, right):
            if len(combination) == 2 * n:
                results.append(''.join(combination))
                return
            if left < n:
                combination.append('(')
                back(combination, left+1, right)
                combination.pop()
            if right < left:
                combination.append(')')
                back(combination, left, right+1)
                combination.pop()
        back([], 0, 0)
        return results