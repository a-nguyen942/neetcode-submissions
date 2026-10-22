class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max, temp_max, left, right = 0, 0, 0, 0
        seen = set()
        n = len(s)
        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                temp_max += 1
            else:
                seen.remove(s[left])
                left += 1
                temp_max -= 1
        
            if curr_max < temp_max:
                curr_max = temp_max
        return curr_max