class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        r, l = k -1, 0

        currentMax = float("-infinity")

        ans = []

        while r < len(nums): 
            
            currentMax = max(nums[l:r +1])
            ans.append(currentMax)
            r = r +1

            l = l + 1


        return ans