class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        summ = 0
        minc = float('inf')

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                minc = min(minc, r - l + 1)
                summ -= nums[l]
                l += 1

        return 0 if minc == float('inf') else minc



        # l = 0
        # r = 0
        # summ = 0
        # minc = float('inf')

        # while l < len(nums):
        #     summ += nums[l]

        #     while summ >= target:
        #         minc = min(minc, l - r + 1)
        #         summ -= nums[r]
        #         r += 1

        #     l += 1

        # return 0 if minc == float('inf') else minc

        # l=0
        # r=0
        # summ=0
        # minc=float('Inf')
        # while l < len(nums):
        #     summ+=nums[l]
        #     while summ >= target:
        #         minc=min(summ, l-r+1)
        #         summ-=nums[r]
        #         r+=1
        #     l+=1
        # return 0 if minc == float('inf') else minc        

            # if l-r+1  < target:
            #     l+=1
            # elif l-r+1 == target:
            #     minc=min(minc,summ)
            #     summ-=nums[r]
            #     r+=1
            #     l+=1                
            # return minc        
                        







        