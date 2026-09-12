class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # loop over s from end and start at same time
        # check lowercase char at start and end pointers
        # skip if non-alphanumeric
        # return false if different chars
        # return true if start pointer >= (len(s) - end pointer index) (they passed or are at middle)
        # time: O(n)
        # space: O(1)

        start_i = 0
        end_i = len(s) - 1

        while start_i < end_i:

            while start_i < end_i and not s[start_i].isalnum():
                start_i += 1
            while start_i < end_i and not s[end_i].isalnum():
                end_i -= 1
            
            if s[start_i].lower() != s[end_i].lower():
                return False
            
            start_i += 1
            end_i -= 1
        
        return True
