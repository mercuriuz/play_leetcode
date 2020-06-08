class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }

        output = []
        def back(combination, digits):
            if len(digits) == 0:
                output.append(combination)
            else:
                for c in mapping[digits[0]]:
                    back(combination + c, digits[1:])
        if len(digits) > 0:
            back("", digits)
        return output