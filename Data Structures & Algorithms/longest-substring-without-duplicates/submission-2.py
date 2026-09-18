class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # init substring start pointer
        l = 0
        sub_chars = set()
        max_len = 0

        for c in s:
            while c in sub_chars: # O(1), max sub_chars is all ascii chars
                sub_chars.remove(s[l])
                l += 1

            sub_chars.add(c)
            max_len = max(max_len, len(sub_chars))

        return max_len

        # time: O(n)
        # space: O(1)
