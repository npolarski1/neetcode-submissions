class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # init dict that keeps track of num indices
        index_dict = {}
        # for each num check if target - num is in dict
        for i, num in enumerate(nums):
            x = target - num

            # if so return indices
            if x in index_dict:
                # saved index will always be smaller than num's
                return [index_dict[x], i]
            
            # if target - num not in dict add num to dict
            index_dict[num] = i
        
        # no default to return since valid answer assumed to exist
        # time: O(n) where n is the size of nums
        # space: O(n) where n is the size of nums