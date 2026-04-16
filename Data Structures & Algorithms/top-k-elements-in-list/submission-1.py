class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts_dict = {}
        for number in nums:
            if number in counts_dict:
                counts_dict[number] += 1
            else:
                counts_dict[number] = 1

        output = []
        sorted_values = sorted(counts_dict.values(), reverse=True)

        # Find elements repeated at least k times
        for key, value in counts_dict.items():
            if counts_dict[key] in sorted_values[:k]:
                output.append(key)
        
        return output
