class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): # impossible for t to be substring if > len
            return ""

        t_counts = {}
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        sub_counts = {}

        l = 0

        res, res_len = "", 100001

        matches = 0

        for r in range(len(s)):
            sub_counts[s[r]] = sub_counts.get(s[r], 0) + 1

            if s[r] in t_counts and sub_counts[s[r]] == t_counts[s[r]]:
                matches += 1

            # while the current substring is valid
            while matches == len(t_counts):

                sub_counts[s[l]] -= 1
                if s[l] in t_counts and t_counts[s[l]] == sub_counts[s[l]] + 1:
                    matches -= 1

                if matches != len(t_counts) and r - l + 1 < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                if l == r:
                    break
                l += 1
        
        return res

        # time: O(n)
        # space: O(1) # 52 max size for count hashmaps (lowercase + uppercase) 
        