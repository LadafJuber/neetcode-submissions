class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0    
        ans=0
        se=set()
        while j < len(s):
            if s[j] not in se:
                se.add(s[j])
                ans=max(ans,j-i+1)
                j+=1
            else:
                while s[j] in se:
                    se.remove(s[i])
                    i+=1
                se.add(s[j])
                j+=1
        return ans

        # win={}
        # l=0
        # max_=0
        # for r in range(len(s)):
        #     win[s[r]] = win.get(s[r],0)+1
        #     while win[s[r]] > 1:
        #         win[s[l]]-=1
        #         l+=1
        #         max_= max(max_,r-l+1)
        # return max_
        