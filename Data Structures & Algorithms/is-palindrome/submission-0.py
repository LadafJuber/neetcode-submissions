class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True                



        # s=s.lower()
        # s=s.replace(" ","")
        # s=s.replace("?","")
        # ta=s
        # l=list(s)
        # left=0
        # right=len(l)-1
        # while left < right:
        #     l[left],l[right]=l[right],l[left]
        #     left+=1
        #     right-=1
        #     k="".join(l)
        #     if ta == k:
        #         return True
        #     else:
        #         return False     