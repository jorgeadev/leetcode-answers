from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Do not modify input list in-place; use a new list for (height, index) tuples
        h_with_idx = [(h, i) for i, h in enumerate(heights)]
        h_with_idx.append((0, len(heights)))  # Sentinel to pop all remaining bars
        stack = []
        max_area = 0
        for height, index in h_with_idx:
            start = index
            while stack and stack[-1][0] > height:
                h, i = stack.pop()
                max_area = max(max_area, h * (index - i))
                start = i
            stack.append((height, start))   
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    heights1 = [2, 1, 5, 6, 2, 3]
    print(f"Input: {heights1}")
    print(f"Output: {solution.largestRectangleArea(heights1)}")  # Expected: 10

    # Example 2
    heights2 = [2, 4]
    print(f"Input: {heights2}")
    print(f"Output: {solution.largestRectangleArea(heights2)}")  # Expected: 4

    # Edge case: all bars of same height
    heights3 = [3, 3, 3, 3]
    print(f"Input: {heights3}")
    print(f"Output: {solution.largestRectangleArea(heights3)}")  # Expected: 12

    # Edge case: increasing heights
    heights4 = [1, 2, 3, 4, 5]
    print(f"Input: {heights4}")
    print(f"Output: {solution.largestRectangleArea(heights4)}")  # Expected: 9

    # Edge case: decreasing heights
    heights5 = [5, 4, 3, 2, 1]
    print(f"Input: {heights5}")
    print(f"Output: {solution.largestRectangleArea(heights5)}")  # Expected: 9
