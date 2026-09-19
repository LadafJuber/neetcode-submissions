class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftm=0
        rightm=0
        water=0
        while left < right:

            if height[left] <= height[right]:

                if height[left] >= leftm:
                    leftm=height[left]
                else:
                    water+=leftm-height[left]
                left+=1    
            else:    
                if height[right] >= rightm:
                        
                    rightm=height[right]
                else:
                    water+=rightm-height[right]
                right-=1
        return water        



        