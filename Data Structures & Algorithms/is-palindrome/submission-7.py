class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # loop over s from end and start at same time
        # check lowercase char at start and end pointers
        # skip if non-alphanumeric
        # return false if different chars
        # return true if start pointer >= (len(s) - end pointer index) (they passed or are at middle)

        start_i = 0
        end_i = len(s) - 1

        while True:
            if start_i >= end_i:
                return True

            while not s[start_i].isalnum():
                start_i += 1

                if start_i >= len(s): # if i goes out of bounds all chars were checked
                    return True
            while not s[end_i].isalnum():
                end_i -= 1

                if end_i < 0: # same here
                    return True
            
            if s[start_i].lower() != s[end_i].lower():
                return False
            
            start_i += 1
            end_i -= 1
