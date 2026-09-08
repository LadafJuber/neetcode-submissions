class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_p=float('inf')
        max_p=0
        
        for p in prices:
            if p < min_p :
                min_p = p
            elif p - min_p > max_p:
                max_p=p-min_p
        if max_p < 0:
            return 0
        else:
            return max_p

        