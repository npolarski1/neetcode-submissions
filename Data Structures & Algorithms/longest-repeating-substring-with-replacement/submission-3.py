class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        import string

        # init char count dict
        count = dict.fromkeys(string.ascii_uppercase, 0)
        # init max substring len tracker
        output = 1
        # init left and right window pointer to 0
        l, r = 0, 0
        # init max frequency for current substring counter
        max_freq = 1

        # while r < len(s)
        while r < len(s):
            # increment count for char at r
            count[s[r]] += 1

            # update max freq
            max_freq = max(max_freq, count[s[r]])

            # if we can replace enough letters to have repeating chars
            if r - l + 1 - max_freq <= k:
                # update max len
                output = max(output, r - l + 1)
                # increment r
                r += 1
            
            # if not
            else:
                while l < r and r - l + 1 - max_freq > k:
                    # sub count for char at l
                    count[s[l]] -= 1
                    # increment l
                    l += 1
                r += 1
        
        # return max len
        return output