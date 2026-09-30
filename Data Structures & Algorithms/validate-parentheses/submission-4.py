class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            '(':")",
            '[':"]",
            '{':"}"
        }

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if len(stack) > 0:
                    if bracket == bracket_map[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

