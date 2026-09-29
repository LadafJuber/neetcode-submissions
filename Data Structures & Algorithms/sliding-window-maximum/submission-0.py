from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):

            # Remove indices outside the window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        # deque=()
        # result=[]
        

        # for i in range(len(nums)):
        #     while deque and deque[0] < i - k+1:
        #         deque.popleft()

        #     while deque and nums[deque[-1]] <nums[i]:
        #         deque.pop()

        #     deque.append(i)    

        #     if i >= k-1:
        #         result.append(nums[deque[0]])
        # return result              