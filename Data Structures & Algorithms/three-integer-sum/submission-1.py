class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort nums
        # init triplet list
        sorted_nums, triplets = sorted(nums), []

        # for n in nums
        for i, n in enumerate(sorted_nums):
            # if n = last num skip, no duplicate triplets
            if i > 0 and n == sorted_nums[i-1]:
                continue

            # init left pointer at start of nums after n
            # init right at end of nums after n
            l, r  = i + 1, len(sorted_nums) - 1

            # while l < r
            while l < r:
                sum = n + sorted_nums[l] + sorted_nums[r]
                # if sum of n and l, r nums > 0 decrement r
                if sum > 0:
                    r -= 1
                # if < 0 increment l
                elif sum < 0:
                    l += 1
                # if == 0, add triplet
                else:
                    triplets.append([n, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1

        # return triplets
        return triplets

        # time: O(n^2)
        # space: O(n)
        
        