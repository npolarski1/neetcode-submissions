class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if their lengths are different we know they aren't anagrams
        if len(s) != len(t):
            return False
        else:
            # create dicts for character counts
            s_count = {}
            t_count = {}

            # index loop so we can loop over s and t at the same time
            for i in range(len(s)):
                s_char = s[i]
                t_char = t[i]

                # increment counter for each char
                s_count[s_char] = s_count.get(s_char, 0) + 1
                t_count[t_char] = t_count.get(t_char, 0) + 1
            
            # check they're equal
            return s_count == t_count
        
        # time: O(n) where n is len(s) and len(t)
        # space: O(1) because char count dicts are never > 26
        #        (since theres 26 lowercase letters)