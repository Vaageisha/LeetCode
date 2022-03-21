class Solution:
    def isValid(self, s: str) -> bool:
        hm,stack = {')': '(', ']': '[', '}': '{'}, []   """hm:  HashMap is a data structure that
                                                         uses a hash function to map identifying values"""

        for i in s:                                          # traverse each paranthesis
            if stack and hm.get(i) == stack[-1]: stack.pop()   # whenever any closing comes, we check we have its opening in top of our stack or not.  
            else:                                 # we will tweak this else part only
                if i in hm: return False         # if i is in hm means we encountered closing and its opening was not there in top of stack, so its false
                stack.append(i)       
        return not stack
