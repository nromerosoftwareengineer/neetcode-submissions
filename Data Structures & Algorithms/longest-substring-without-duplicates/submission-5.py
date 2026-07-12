class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag_of_unique_chars = set()
        max_size = 1
        if(len(s) < 1):
            return 0

        l = 0
        r = 0

        while r < len(s):

            while s[r] in bag_of_unique_chars:
                bag_of_unique_chars.remove(s[l])
                l +=1
            max_size = max(r-l +1, max_size)
            bag_of_unique_chars.add(s[r])
            r +=1

        return max(max_size, len(bag_of_unique_chars) )
        