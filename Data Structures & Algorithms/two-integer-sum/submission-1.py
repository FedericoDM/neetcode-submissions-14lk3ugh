class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = 0
        for index in range(len(nums)):
            num_1 = nums[index]
            if index < len(nums) - 1:
                for other_index in range(index + 1, len(nums)):
                    num_2 = nums[other_index]
                    if num_1 + num_2 == target:
                        return [index, other_index]
