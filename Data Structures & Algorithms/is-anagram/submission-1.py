class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if(s[i] not in my_dict):
                my_dict[s[i]] = 1
            else:
                my_dict[s[i]] += 1

        for i in range(len(t)):
            if(t[i] not in my_dict):
                return False
            else:
                my_dict[t[i]] -= 1
                if my_dict[t[i]] == 0:
                    my_dict.pop(t[i])

        return True
        