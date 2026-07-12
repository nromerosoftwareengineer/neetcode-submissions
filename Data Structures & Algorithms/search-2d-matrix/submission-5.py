class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = self.findRow(matrix, target)
        if row:
            return self.binarySearch(row, target)
        else:
            return False

    def findRow(self, matrix: List[List[int]], target: int) -> List[int]:
        l = 0
        r = len(matrix[0]) -1 

        for row in matrix:
            if row[l] <= target and target <= row[r]:
                return row
        return None

    def binarySearch(self, row:List[int], target:int) -> bool:
        l = 0
        r = len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] > target: 
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
               return True
        return False 
            