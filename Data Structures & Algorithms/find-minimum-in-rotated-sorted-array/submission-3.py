class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1

        minVal = 1001
        # [4,5,6,7] 
       # m = 1  = 5

  

        while l < r:
            m = (l + r) // 2
            # 5 <= 7
            if nums[m] <= nums[r]:
                r = m -1
                minVal = min(minVal, nums[r])
            else:
                l = m + 1
                minVal = min(minVal, nums[l])
           
            minVal = min(minVal, nums[m])

        if len(nums) == 1:
            return nums[0]
        return minVal