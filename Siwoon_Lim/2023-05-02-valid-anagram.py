class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for s_char in set(s):
                if s.count(s_char) != t.count(s_char):
                    return False
            return True
        else:
            return False