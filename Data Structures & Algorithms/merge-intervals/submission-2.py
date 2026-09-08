class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the intervals so that overlapping intervals are consecutive
        # init merged interval list to be output with intervals[0]
        # loop over intervals (staring from interval[1])
        # check if current interval overlaps with last interval in merged
        # if so update last merged interval
        # if not append to merged list
        # return merged list

        intervals.sort(key=lambda i: i[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start, end])

        return merged

        # time: O(nlogn)
        # space: O(n)
