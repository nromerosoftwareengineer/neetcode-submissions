class Solution:
    def isValid(self, s: str) -> bool:

        l = 0 
        stack = []
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        while l < len(s): 
            if s[l] in pairs:
                stack.append(s[l])

            else:


                if len(stack) >= 1 and pairs[stack[-1]]  == s[l]:
                    stack.pop(-1)
                else:
                    return False

            l +=1

        return len(stack) < 1