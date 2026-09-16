class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # init nums set
        nums_set = set(nums)

        # init longest sequence tracker to 0
        longest = 0

        # iterate over nums
        for n in nums:
            # if num - 1 not in set num is start of sequence
            if n - 1 not in nums_set:
                # set sequence length to 1
                seq_len = 1

                # while sequence num + 1 is in nums set
                while n + seq_len in nums_set:
                    # increment sequence len
                    seq_len += 1

                # if sequence len > longest set longest to sequence len
                longest = max(seq_len, longest)

        # return longest sequence len
        return longest

        # time: O(n) because inner while loop will never execute more than
        # n times
        # space: O(n)
                