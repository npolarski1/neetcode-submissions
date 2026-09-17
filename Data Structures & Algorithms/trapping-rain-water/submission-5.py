class Solution:
    def trap(self, height: List[int]) -> int:
        
        # init left pointer at start of height
        # init right poitner at end of height
        l, r = 0, len(height) - 1

        # set left max to first height
        # set right max to right height
        l_max, r_max = height[0], height[-1]

        # init total water to 0
        total = 0

        # while l < r:
        while l < r:
            # get water at min left, right h (min left right max - h)
            h = min(height[l], height[r])
            h_water = min(l_max, r_max) - h

            # if postive add to total water
            total += max(0, h_water)

            # check if new max
            l_max = max(height[l], l_max)
            r_max = max(height[r], r_max)

            # move min left right pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # return total water
        return total