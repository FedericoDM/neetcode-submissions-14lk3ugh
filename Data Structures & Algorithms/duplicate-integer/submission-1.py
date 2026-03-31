class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_set = len(set(nums))
        print(set(nums))
        return length_set != len(nums)