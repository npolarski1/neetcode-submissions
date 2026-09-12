class Solution:
    def isValid(self, s: str) -> bool:
        
        # init stack
        # if left bracket push to stack
        # if right pop from stack and check that its equal to current char

        stack = []

        for b in s:
            if b == "(" or b == "{" or b == "[":
                stack.append(b)
            elif len(stack) == 0: # must be right bracket
                return False
            elif ((b == ")" and stack.pop() != "(") 
               or (b == "}" and stack.pop() != "{") 
               or (b == "]" and stack.pop() != "[")):
                return False
            
        if len(stack) != 0:
            return False
        return True
