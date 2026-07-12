class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        bag_of_chars = 26 * [0]
        l,r = 0,0
        maxLength = 0
        originalK = k
        s = s.lower()
        def maxfreqCharacter(bag_of_chars:list) -> int:
            return max(range(26), key=lambda i: bag_of_chars[i])


        while r < len(s):
            print("r = ", str(r))
            print("s[r] = ", s[r])
            print("ord(s[r]) - ord('a') = ", str(ord(s[r]) - ord('a')) )
            bag_of_chars[ord(s[r]) - ord('a')] += 1
            maxfreqChar = maxfreqCharacter(bag_of_chars)

            subStringLength = ( r -l +1)
            while not((subStringLength - bag_of_chars[maxfreqChar] ) <= k):
                bag_of_chars[ord(s[l]) - ord('a')] -= 1
                l +=1
                subStringLength = ( r -l +1)
                maxfreqChar = maxfreqCharacter(bag_of_chars)
            maxLength = max(subStringLength, maxLength)
            r +=1
        print(bag_of_chars)
        return maxLength

        