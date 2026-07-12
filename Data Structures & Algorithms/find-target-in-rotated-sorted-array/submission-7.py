class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r= len(nums) -1 



        while l + 1 < r: 
            m = (l + r) // 2 

            if nums[m] == target:
                return m
            # left is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: 
                    r = m
                    
                else: 
                     l = m
            # right is sorted         
            else: 
                if nums[m] < target <= nums[r]: 
                    l = m 
                else: 
                    r = m 

        if nums[l] == target:
            return l 
        elif nums[r] == target: 
            return r
        else: 
            return -1

        
        