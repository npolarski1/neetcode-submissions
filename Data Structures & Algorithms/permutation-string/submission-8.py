class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string

        if len(s1) > len(s2): # s2 can't contain s1 if s1 is longer
            return False

        s1_count = {c : 0 for c in string.ascii_lowercase}
        window_count = {c : 0 for c in string.ascii_lowercase}
        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            window_count[s2[i]] +=1
        
        l, r = 0, len(s1) - 1

        while r < len(s2):
            if s1_count == window_count: # O(1) since counts len == 26
                return True

            r += 1
            if r == len(s2): 
                return False
            window_count[s2[r]] += 1

            window_count[s2[l]] -= 1
            l += 1

        return False

        # time: O(n)
        # space: O(1)

            