class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        r=1    
        for w in range(1,len(nums)):
            if nums[w] != nums[w-1]:
                nums[r] = nums[w]
                r+=1
        return r      