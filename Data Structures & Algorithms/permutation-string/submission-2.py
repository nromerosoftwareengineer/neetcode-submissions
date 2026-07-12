class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        bag_of_chars_s1 = 26 * [0]
        bag_of_chars_s2 = 26 * [0]
        matches = 0

        if(len(s1) > len(s2)):
            return False

        for i in range(len(s1)):
            bag_of_chars_s1[ord(s1[i]) - ord('a')] += 1
            bag_of_chars_s2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if bag_of_chars_s1[i] == bag_of_chars_s2[i]:
                matches +=1

        l,r = 0, len(s1)

        while r < len(s2):
            if matches == 26 : return True
            index = ord(s2[r]) - ord('a')

            bag_of_chars_s2[index] +=1
            if bag_of_chars_s1[index] == bag_of_chars_s2[index]:
                matches +=1
                
            elif bag_of_chars_s1[index] + 1 == bag_of_chars_s2[index]:
                matches -=1

            index = ord(s2[l]) - ord('a')
            bag_of_chars_s2[index] -=1
            if bag_of_chars_s1[index]  == bag_of_chars_s2[index]:
                matches +=1
            elif bag_of_chars_s1[index] - 1 == bag_of_chars_s2[index]:
                matches -=1

            r +=1
            l +=1
        return matches == 26
            


        print(matches)
        
        return False

           


        