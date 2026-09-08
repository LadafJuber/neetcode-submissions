class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        def revrse(l,r):
            while l < r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        revrse(0,n-1)
        revrse(0,k-1)
        revrse(k,n-1)



        
        