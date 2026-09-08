class Solution:
    def isPalindrome(self, s: str) -> bool:
        re="".join(c for c in s if c.isalnum())
        x=re.lower()
        
        left=0
        right=len(x)-1
        while left <= right:
            
            if x[left] != x[right]:
                return False
             
            left+=1
            right-=1
        return True          

        