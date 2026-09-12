class Solution:
    def isValid(self, s: str) -> bool:
        
        # init stack
        # init open-close bracket matching dict
        # if left bracket push to stack
        # if right pop from stack and check that its equal to current char

        stack = [] # O(n)
        match = {")": "(", "}": "{", "]": "["}

        for b in s: # O(n)
            if b in match:
                if len(stack) == 0 or stack.pop() != match[b]:
                    return False
            else:
                stack.append(b)
                
        if len(stack) != 0:
            return False
        return True
