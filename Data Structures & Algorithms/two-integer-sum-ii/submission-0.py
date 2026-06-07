class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while left_pointer< len(numbers):
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer += -1
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1
            else:
                # Add one since problem statement says it is a 1-indexed array
                solution = [left_pointer + 1, right_pointer + 1]
                return solution
