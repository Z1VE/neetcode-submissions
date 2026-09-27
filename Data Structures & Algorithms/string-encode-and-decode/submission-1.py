from typing import List

class Solution: 
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_result = []
        
        for word in strs:
            # 1. Shift characters by +5
            jumbled_word = "".join(chr(ord(char) + 5) for char in word)
            # 2. Store as "length#jumbled_word"
            encoded_result.append(f"{len(jumbled_word)}#{jumbled_word}")
            
        return "".join(encoded_result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string back to a list of strings."""
        decoded_list = []
        i = 0
        
        while i < len(s):
            # 1. Find the delimiter to get the length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            
            # 2. Extract the jumbled word based on the length
            start_word = j + 1
            end_word = start_word + length
            jumbled_word = s[start_word:end_word]
            
            # 3. Shift characters back by -5
            original_word = "".join(chr(ord(char) - 5) for char in jumbled_word)
            decoded_list.append(original_word)
            
            # 4. Move pointer to the next encoded block
            i = end_word
            
        return decoded_list
