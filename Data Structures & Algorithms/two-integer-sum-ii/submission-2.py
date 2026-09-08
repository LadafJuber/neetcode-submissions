class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r=0,len(numbers)-1
        m=[]
        while l < r:
            sum= numbers[l] + numbers[r]
            if  sum > target:
                r-=1
            elif sum  < target:
                l+=1
            else:
                return [l+1,r+1]          
                
        return []
                       



        # m=[]
        # for i in range(1,len(numbers)):
        #     j=i-1
        #     if numbers[i]+numbers[j] == target:
        #         m.append(numbers[j])
        #         m.append(numbers[i])                
        return m    


        