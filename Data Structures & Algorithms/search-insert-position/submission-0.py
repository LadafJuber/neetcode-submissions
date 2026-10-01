class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        hight=len(nums)
        while low < hight:
            mid = (low+hight) //2
            if nums[mid] < target:
                
                low=mid+1
            else:
                hight=mid
        return low            

        