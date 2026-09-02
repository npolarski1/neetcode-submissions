class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if their lengths are different we know they aren't anagrams
        if len(s) != len(t):
            return False
        else:
            # sort strings in alphabetical order
            # check they're equal
            return sorted(s) == sorted(t)
        
        # time: O(nlogn + mlogm)
        # space: O(1)
            