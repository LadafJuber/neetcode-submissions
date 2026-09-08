class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def idx(c):
            return ord(c) - ord('a')

        count1 = [0] * 26
        count2 = [0] * 26

        for c in s1:
            count1[idx(c)] += 1

        # first window
        for c in s2[:len(s1)]:
            count2[idx(c)] += 1

        if count1 == count2:
            return True

        # sliding window
        for i in range(len(s1), len(s2)):
            count2[idx(s2[i])] += 1
            count2[idx(s2[i - len(s1)])] -= 1

            if count1 == count2:
                return True

        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False

#         s1c ,s2c =[0]*26,[0]*26
#         for i in range(len(s1)):
#             s1c[ord(s1[i])-ord('a')] +=1
#             s2c[ord(s2[i]) -ord('a')] +=1

#         match=0
#         for i in range(26):
#             match+=(1 if s1c[i] == s2c[i] else 0 )

#         l=0
#         for r in range(len(s1),len(s2)):
#             if match == 26:
#                 return True

#             index = ord(s2[r]) - ord('a')  
#             s2c[index] +=1
#             if s1c[index] == s2c[index]:
#                 match +=1
#             elif s1c[index] +1 == s2c[index]:
#                 match -=1

#             index = ord(s2[l]) - ord('a')
#             s2c[index] -=1
#             if s1c[index] == s2c[index]:
#                 match+=1
#             elif s1c[index] -1 == s2c[index]:
#                 match -=1
#             l+=1
#         return match == 26            




        


        
        

        