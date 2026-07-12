
"""
1) have a freq map 
2) sliding window 
3) capture max freq 
4) pop from left when k threshold is met and reduce frequency of poped index 

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = [0 for _ in range(26)]
        

        current_max_letter = 0
        windowCount = 0
        maxFreqindx = ord(s[0]) - ord("A")
        

        l = 0
#      "AAABABB"
        for r in range(len(s)):
            indx = ord(s[r]) - ord("A")
            freq_map[indx] += 1

            

            if freq_map[indx] > freq_map[maxFreqindx]:
                maxFreqindx = indx

            if  (r -l + 1) - freq_map[maxFreqindx] > k:
                freq_map[ord(s[l]) - ord("A")] -=1
                l +=1 
            windowCount = max((r -l + 1), windowCount)


        return windowCount
        