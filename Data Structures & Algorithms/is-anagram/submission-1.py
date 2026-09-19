class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = [0] * 26
        t_counter = [0] * 26

        if len(s) != len(t):
            return False
        

        for i in range(len(s)):
            s_counter[97 - ord(s[i])] += 1
            t_counter[97 - ord(t[i])] += 1
        
        for i in range(len(s_counter)):
            if s_counter[i] != t_counter[i]:
                return False
        return True
        