from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [*nums, *nums]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.getConcatenation(nums1)}")  # Expected: [1, 2, 1, 1, 2, 1]

    # Example 2
    nums2 = [1, 3, 2, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.getConcatenation(nums2)}")  # Expected: [1, 3, 2, 1, 1, 3, 2, 1]

    # Edge case: empty array
    nums3 = []
    print(f"Input: {nums3}")
    print(f"Output: {solution.getConcatenation(nums3)}")  # Expected: []

    # Edge case: single element
    nums4 = [5]
    print(f"Input: {nums4}")
    print(f"Output: {solution.getConcatenation(nums4)}")  # Expected: [5, 5]