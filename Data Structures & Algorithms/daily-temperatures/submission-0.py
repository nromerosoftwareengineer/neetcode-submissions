class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)

        stack = []
       
        print(ans)
        for index, n  in enumerate(temperatures):   
             print(n, index)         
             while stack and n > temperatures[stack[-1]]:      
                ans[stack[-1]] = index - stack[-1]
                stack.pop(-1)
             stack.append(index)
        return ans
            