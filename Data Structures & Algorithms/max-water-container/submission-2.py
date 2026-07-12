class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights) -1 
        max_left = heights[l]
        max_right = heights[r]

        max_water = -1 
        cur_water = -1 

        while l < r: 
            cur_water = min(heights[l] , heights[r]) * (r - l )
            

            max_water = max( cur_water, max_water) 
            if heights[l] >= heights[r]:
                r -=1
            else:
                l +=1


        return max_water
            
        