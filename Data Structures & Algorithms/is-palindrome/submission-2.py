class Solution:
    def isPalindrome(self, s: str) -> bool:
        # re="".join(c for c in s if c.isalnum())
        # x=re.lower()
        
        # left=0
        # right=len(x)-1
        # while left <= right:
            
        #     if x[left] != x[right]:
        #         return False
             
        #     left+=1
        #     right-=1
        # return True                 
        left=0
        right=len(s)-1
        while left <= right:
            while left < right and not s[left].isalnum():
                left+=1
            while  left < right and not s[right].isalnum():
                right-=1

            
            if s[left].lower() != s[right].lower():
                return False
             
            left+=1
            right-=1
        return True 

        