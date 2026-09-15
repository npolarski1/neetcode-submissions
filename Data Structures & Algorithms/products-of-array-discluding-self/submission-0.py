class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # init output with same len as nums
        output = [1] * len(nums)

        # init prefix product to 1
        pre = 1
    
        # loop over nums[1:], let index be i
        for i in range(1, len(nums)):
            # prefix *= nums[i - 1]
            pre *= nums[i - 1]
            # set output[i] to prefix
            output[i] = pre

        # init postfix product to 1
        post = 1
        # loop over nums[:-1] right to left
        for i in range(len(nums) - 2, -1, -1):
            # postfix *= nums[i + 1]
            post *= nums[i + 1]
            # output[i] *= postfix
            output[i] *= post

        # return output
        return output
