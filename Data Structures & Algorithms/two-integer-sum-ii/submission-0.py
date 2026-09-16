class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # init pointer at start of numbers
        l = 0
        # init pointer at end of numbers
        r = len(numbers) - 1

        # while left pointer < right pointer
        while l < r:
            sum = numbers[l] + numbers[r]

            # if sum < target
            if sum < target:
                # increment left pointer
                l += 1
            # if sum > target
            elif sum > target:
                # decrement right pointer
                r -= 1
            # if sum == target
            else:
                # return pointers
                return [l + 1, r + 1]

        # time: O(n)
        # space: O(1)
