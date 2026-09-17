class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # init max area tracker
        max_area = 0
        # set left pointer to start of heights
        l = 0
        # set right pointer to end of heights
        r = len(heights) - 1

        # while l < r
        while l < r:
            # calculate area
            area = min(heights[l], heights[r]) * (r - l)

            # if area > max area
            # set max area to current area
            max_area = max(max_area, area)

            # check current height for left
            # check current height for right
            # move left or right with max current height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        # return max area
        return max_area

        # time: O(n)
        # space O(1)