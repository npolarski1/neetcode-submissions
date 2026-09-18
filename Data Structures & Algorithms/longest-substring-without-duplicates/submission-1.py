class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        
        max_len = 0
        sub_deque = deque()
        sub_chars = set()

        for c in s:
            while c in sub_chars: # O(1), max sub_chars is all ascii chars
                sub_chars.remove(sub_deque.popleft())

            sub_deque.append(c)
            sub_chars.add(c)
            max_len = max(max_len, len(sub_deque))

        return max_len

        # time: O(n)
        # space: O(n)
