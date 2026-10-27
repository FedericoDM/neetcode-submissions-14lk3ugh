class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets 
        [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
        and the indices i, j and k are all distinct.
        """
        # First, sort the array
        sorted_nums = sorted(nums)
        solutions = []

        # Rearranging into an equation, it would be something like:
        # nums[i] + nums[j] = -nums[k]
        for index_k in range(0, len(sorted_nums)):
            if index_k > 0 and sorted_nums[index_k] == sorted_nums[index_k - 1]:
                continue
            target = -(sorted_nums[index_k])
            left_pointer = index_k + 1
            right_pointer = len(sorted_nums) - 1
            while left_pointer < right_pointer:
                pointer_sum = (
                    sorted_nums[left_pointer] + sorted_nums[right_pointer]
                )
                if pointer_sum > target:
                    right_pointer += -1
                elif pointer_sum < target:
                    left_pointer += 1
                else:
                    solution = [
                        sorted_nums[left_pointer], sorted_nums[right_pointer], -target
                        ]
                    solutions.append(solution)
                    # Look for multiple solutions
                    while left_pointer < right_pointer and sorted_nums[left_pointer] == solution[0]:
                        left_pointer += 1
                    while left_pointer < right_pointer and sorted_nums[right_pointer] == solution[1]:
                        right_pointer -= 1
        
        return solutions
