class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Obtain maximum possible area
        """
        left_pointer = 0
        right_pointer = len(heights) - 1
        max_area = 0

        while left_pointer < right_pointer:

            left_bar = heights[left_pointer]
            right_bar = heights[right_pointer]

            width = right_pointer - left_pointer
            height = min(left_bar, right_bar)

            area = width * height

            if area > max_area:
                max_area = area

            if left_bar < right_bar:
                left_pointer += 1

            elif left_bar > right_bar:
                right_pointer += -1

            else:
                left_pointer += 1

        return max_area