import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        final_output = []
        for index in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(index)
            final_output.append(math.prod(nums_copy))

        return final_output





        