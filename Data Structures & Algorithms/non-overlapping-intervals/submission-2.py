class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # init removal count
        # sort intervals by start
        # loop over intervals
        # compare adjacent intervals
        # if they overlap skip the one that ends later, increment counter
        # return count

        removals = 0

        intervals.sort(key=lambda i: i[0]) # O(nlogn)

        prev_end = intervals[0][1]
        for i in intervals[1:]: # first has no prev to check against
            if i[0] < prev_end:
                prev_end = min(i[1], prev_end)
                removals += 1
            else:
                prev_end = i[1]
        
        return removals
