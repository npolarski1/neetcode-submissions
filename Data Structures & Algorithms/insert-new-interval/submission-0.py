class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # init output list with new interval
        # loop over intervals
        # merge current with output[-1] if overlapping
        # if not check if it comes before or after
        # if before set output[-1] to current, append previous output[-1]
        # if after just append current

        output = [newInterval]

        for start, end in intervals:
            if start <= output[-1][1] and end >= output[-1][0]:
                output[-1] = [min(start, output[-1][0]), max(end, output[-1][1])]
            else:
                if start < output[-1][0]:
                    prevLast = output[-1]

                    output[-1] = [start, end]
                    output.append(prevLast)
                else:
                    output.append([start, end])

        return output
