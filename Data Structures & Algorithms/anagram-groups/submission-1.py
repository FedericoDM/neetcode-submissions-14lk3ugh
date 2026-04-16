class Solution:

    @staticmethod
    def count_characters(string: str) -> dict:
        """
        Counts number of characters in string
        """
        final_dict = {}
        for character in sorted(string):
            if character in final_dict:
                final_dict[character] += 1
            else:
                final_dict[character] = 1
        
        return final_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_output = []
        res = collections.defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        
        for key in res:
            final_output.append(res[key])

        return final_output
