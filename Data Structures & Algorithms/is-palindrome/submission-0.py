class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.replace(' ','').lower()
        result = ''
        for char in clean:
            if char.isalnum():
                result += char
        
        reversed = result[::-1]
        return result == reversed