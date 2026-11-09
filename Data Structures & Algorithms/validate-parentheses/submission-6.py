class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {
            "}": "{", 
            ")": "(",
            "]": "["
        }
        for index in range(len(s)):
            if stack and stack[-1] == close_to_open.get(s[index]):
                stack.pop()
            else:
                stack.append(s[index])
        
        return False if stack else True


        