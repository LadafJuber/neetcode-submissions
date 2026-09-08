class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        leftm=0
        rightm=0
        water=0
        while left < right:
            if height[left] <= height[right]:
                leftm=max(height[left],leftm)
                water+=leftm-height[left]
                left+=1
            else:
                rightm=max(height[right],rightm)
                water+=rightm-height[right]
                right-=1
        return water        

        