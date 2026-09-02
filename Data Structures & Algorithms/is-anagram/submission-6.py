class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if their lengths are different we know they aren't anagrams
        if len(s) != len(t):
            return False
        else:
            # sort strings in alphabetical order
            s = sorted(s)
            t = sorted(t)
            # check they're equal
            return s == t
        
        # time: O(nlogn + mlogm)
        # space: O(1)
            