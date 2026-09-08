class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the intervals so that overlapping intervals are consecutive
        # loop over intervals
        # check if next interval overlaps
        # if so remove next interval and change current to merged
        # check next interval until they can't be merged
        # return intervals

        intervals.sort(key=lambda i: i[0])

        i = 0
        while i < len(intervals) - 1:
            current = intervals[i]
            next = intervals[i+1]

            while current[0] <= next[1] and next[0] <= current[1]:
                current = [current[0], max(current[1], next[1])]

                intervals[i] = current
                del intervals[i+1]

                if i >= len(intervals) - 1:
                    break

                next = intervals[i+1]
            i += 1

        return intervals
