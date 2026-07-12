import sys
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       

        l = 1
        r = max(piles)
        k = sys.maxsize
     
        while l <= r:
            m = (l + r) // 2
            t = self.totalHours(m, piles)
            if t > h:
                #increment the left bound
                l = m + 1
            else:
                k = min(k, m)
                r = m -1
        return k

    def totalHours(self, m:int, piles: List[int])-> int:
        total = 0
        for p in piles:
            total += math.ceil(p / m)   # regular division so ceil actually rounds up
        return total

        