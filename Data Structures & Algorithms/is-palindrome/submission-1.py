import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        if len(cleaned_s) < 2: return True # case for empty string and str length 1
        i, j = 0, len(cleaned_s) - 1
        while i < j:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i += 1
            j -= 1
        return True