class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init array of most common nums
        res = [] * k

        # init counter array (size of 2001 for -1000 to 1000)
        count = [0] * 2001

        # loop over nums
        for n in nums:
            # increment counter
            count[n + 1000] += 1
        
        # loop k times:
        for i in range(k):
            # find num with max count
            i = count.index(max(count))

            # add to results
            res.append(i - 1000)

            # set count to 0
            count[i] = 0

        # return results
        return res
 