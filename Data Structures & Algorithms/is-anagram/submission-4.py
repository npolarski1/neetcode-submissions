class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if their lengths are different we know they aren't anagrams
        if len(s) != len(t):
            return False
        else:
            # sort strings in alphabetical order
            s_sorted = sorted(s)
            t_sorted = sorted(t)
            # check they're equal
            return s_sorted == t_sorted
            