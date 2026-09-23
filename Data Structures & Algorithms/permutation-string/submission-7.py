class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string

        if len(s1) > len(s2):
            return False

        # init s1 char count dict
        s1_count = {c : 0 for c in string.ascii_lowercase}
        # loop over s1 and update counts
        for c in s1:
            s1_count[c] += 1
        
        # init sliding window char count dict
        window_count = {c : 0 for c in string.ascii_lowercase}
        # init l and r to 0
        l, r = 0, 0
        # increase window until it equals s1 len and update counts
        while r < len(s1):
            window_count[s2[r]] += 1
            r += 1
        r -= 1

        # while r < s2 len
        while r < len(s2):
            # check if current window
            if s1_count == window_count: # O(1) since counts len == 26
                return True

            # increment r
            r += 1
            # check if r passed edge of s2
            if r == len(s2):
                return False
            # increment r char count
            window_count[s2[r]] += 1

            # decrement l char count
            window_count[s2[l]] -= 1
            # increment l
            l += 1

        # no permutation found
        return False

        # time: O(n)
        # space: O(1)

            