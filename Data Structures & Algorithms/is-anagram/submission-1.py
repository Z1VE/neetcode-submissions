class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_textA = "".join(sorted(s))
        sorted_textB = "".join(sorted(t))

        if sorted_textA == sorted_textB:
            return True
        else:
            return False