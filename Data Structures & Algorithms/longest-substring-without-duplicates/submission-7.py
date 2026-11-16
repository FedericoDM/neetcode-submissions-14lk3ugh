class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Calculates the length of longest substring
        """
        char_set = set()
        result = 0
        left = 0

        for right in range(len(s)):
            # Check if duplicate
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            result = max(result, right - left + 1)

        return result

    def _lengthOfLongestSubstring(self, s: str) -> int:
        """
        Calculates the length of longest substring
        """
        lengths = []
        index = 0
        length = 1
        seen_chars = set()
        
        if len(s) == 0:
            return 0

        elif len(s) == 1:
            return 1

        while index < len(s) - 1:
            char = s[index]
            seen_chars.add(char)
            
            next_index = index + 1
            next_char = s[next_index]

            while (next_char not in seen_chars):
                length += 1
                seen_chars.add(next_char)
                next_index += 1
                if next_index <= len(s) - 1:
                    next_char = s[next_index]
                else:
                    break

            lengths.append(length)
            length = 1
            seen_chars = set()
            index += 1

        return max(lengths)
