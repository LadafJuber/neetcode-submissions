class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start=0
        curr_sum=0
        min_len=float('inf')

        for i in range(len(nums)):
            curr_sum+=nums[i]

            while curr_sum >= target:
                min_len=min( min_len,i - start+1)
                curr_sum-=nums[start]
                start+=1

        return min_len if min_len != float('inf') else 0         

