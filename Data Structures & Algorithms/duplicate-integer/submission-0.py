class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # init num set to check for duplicates against 
        # O(1) time complexity
        duplicate_set = set()

        # loop over nums and add to duplicate_set
        for num in nums:
            # if num in duplicate_set return true
            if num in duplicate_set:
                return True
            # if not add to duplicate_set
            else:
                duplicate_set.add(num)

        # if whole list is processed, 
        # then we know theres no duplicates
        return False
        