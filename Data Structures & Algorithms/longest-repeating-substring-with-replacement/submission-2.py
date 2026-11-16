class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        You are given a string s consisting of only uppercase english characters and an integer k. 
        
        You can choose up to k characters of the string and replace them with
        any other uppercase English character.
        
        After performing at most k replacements, return the length of the longest
        substring which contains only one distinct character.
        """
        # Count occurrences 

        element_ocurrences = {}
        left = 0
        result = 0

        for right in range(len(s)):
            element_ocurrences[s[right]] = 1 + element_ocurrences.get(s[right], 0)
            # Check if the window is valid: number of replacements to do > allowed (k)
            while (right - left + 1) - max(element_ocurrences.values()) > k:
                # Move window, s[left] is not on the window so decrease its count
                element_ocurrences[s[left]] += -1
                left += 1

            # Max result
            result = max(result, right - left + 1)

        return result
            
