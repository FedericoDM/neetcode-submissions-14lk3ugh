class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if the string is a valid palindrome or not
        """

        # Clean non alphanumeric elements, reverse cleaned text
        clean_string = ''.join(filter(str.isalnum, s))
        clean_string = clean_string.lower()
        reverse_string = clean_string[::-1]

        # If palindrome, character and reverse character will always be the same
        for character, reverse_character in zip(clean_string, reverse_string, strict=True):
            if character != reverse_character:
                return False

        return True