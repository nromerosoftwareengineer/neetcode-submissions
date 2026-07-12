class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) -1

        print("nums value: ", nums)
        while low <= high:
            mid = (low + high)//2 

            if nums[mid] < target:
                # target hit
                 #target is greater than mid
                low = mid +1
            elif nums[mid] > target:
                #target is greater than mid
                high = mid - 1
               
            else:
               return mid
               
        return -1 