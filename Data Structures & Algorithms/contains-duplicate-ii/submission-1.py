class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        seen = {} 
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
    
        # for i in range(1,len(nums)-1):
        #     j=0
        #     while j < len(nums)-1 :
        #         if nums[j] == nums[i] and abs(j-i) <= k:                    
        #             return True
        #         else:
        #             return False
        #         j+=1    


                        






        
        