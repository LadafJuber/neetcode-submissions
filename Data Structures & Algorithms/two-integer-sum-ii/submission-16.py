class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total < target:
                left += 1

            else:
                right -= 1

        # seen = {}

        # for i, num in enumerate(numbers):
        #     diff = target - num

        #     if diff in seen:
        #         return [seen[diff], i]

        #     seen[num] = i
 
        # numbers.sort()
        # left=0
        # right=len(numbers)-1

        # while left < right:
        #     s=numbers[left]+numbers[right]
        #     if  s == target:
        #         return [numbers[left],numbers[right]]
        #     elif s < target:
        #         left+=1
        #     else:
        #         right-=1
        # return []
        
                


        