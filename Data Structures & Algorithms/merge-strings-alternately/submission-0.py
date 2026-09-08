class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=len(word1)
        r=len(word2)
        m=0
        n=0
        re=""
        while m < l or n < r:
            if m < l :
                re+=word1[m]
                m+=1
            if n < r:
                re+=word2[n]
                n+=1
        return re        

