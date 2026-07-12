class Solution:
    def minWindow(self, s: str, t: str) -> str:
        current_window, string_window = {}, {}
        current_matches = 0
        need_matches = len(t)

        ans_length = float("infinity")
        current_sub = ""
        ans = ""
        for c in t: 
            if c in string_window:
                string_window[c] +=1 
            else:
                string_window[c] = 1 

        l=0
        for r in range(len(s)):

            if s[r] in current_window:
                current_window[s[r]] = current_window[s[r]] + 1
            else:
                current_window[s[r]] = 1
            # check if there is a match in character count 
            if s[r] in string_window and current_window[s[r]] <= string_window[s[r]]:
                current_matches += 1
            

            while current_matches >= need_matches: 
                ans = s[l:r +1] if (r -l +1) < ans_length else ans
                ans_length = min((r -l +1), ans_length)

                current_window[ s[l] ] = current_window[s[l]] - 1
                if s[l] in t and current_window[s[l]] < string_window[s[l]]:
                    current_matches -=1
                
                l +=1 

            


        return ans

            
        