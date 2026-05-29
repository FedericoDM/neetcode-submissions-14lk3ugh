class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Gets the length of the longest consecutive sequence
        of elementes
        """
        # Get sorted, unique list
        sorted_nums = sorted(list(set(nums)))
        print(sorted_nums)
        # Build counter and dict
        num_sequence = 0
        consecutive_lens = {
            "0": 0
        }
        # Add first element if there is any
        if sorted_nums:
            consecutive_lens[str(num_sequence)] += 1
        for index in range(0, len(sorted_nums)):
            if index >= 1:
                difference = abs(sorted_nums[index] - sorted_nums[index - 1])
                if difference == 1:
                    consecutive_lens[str(num_sequence)] += 1
                # consecutiveness is lost, we start a new sequence
                else:
                    num_sequence += 1
                    if num_sequence in consecutive_lens:
                        consecutive_lens[str(num_sequence)] += 1
                    else:
                        consecutive_lens[str(num_sequence)] = 1

        return max(consecutive_lens.values())


