class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        window = deque()
        output = []
        for i, n in enumerate(nums):
            while len(window) != 0 and window[-1][1] < n:
                window.pop()
            
            window.append((i, n))

            if i >= k - 1:
                # check if stored max is outside of window now
                if window[0][0] == i - k:  
                    window.popleft()
                output.append(window[0][1])
                if len(window) == k:
                    window.popleft()

        return output
        
        