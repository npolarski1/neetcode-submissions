class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): # impossible for t to be substring if > len
            return ""

        t_counts, sub_counts = {}, {}
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1

        l = 0

        res, res_len = [-1, -1], 100001

        matches = 0

        for r in range(len(s)):
            c = s[r]
            sub_counts[c] = sub_counts.get(c, 0) + 1

            if c in t_counts and sub_counts[c] == t_counts[c]:
                matches += 1

            # while the current substring is valid
            while matches == len(t_counts):
                if r - l + 1 < res_len:
                    res[0] = l
                    res[1] = r
                    res_len = r - l + 1

                sub_counts[s[l]] -= 1
                if s[l] in t_counts and t_counts[s[l]] == sub_counts[s[l]] + 1:
                    matches -= 1

                if l == r:
                    break
                l += 1
        
        return s[res[0] : res[1] + 1]

        # time: O(n)
        # space: O(1) # 52 max size for count hashmaps (lowercase + uppercase) 
        