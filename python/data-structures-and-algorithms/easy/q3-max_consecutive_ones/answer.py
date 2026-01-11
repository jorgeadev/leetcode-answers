from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        last = 0
        plus = 0
        for i in nums:
            if (i == 0):
                last = max(last, plus)
                plus = 0
            else:
                plus += 1
                last = max(last, plus)
        return last
    

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 1, 0, 1, 1, 1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums1)}")  # Expected: 3

    # Example 2
    nums2 = [1, 0, 1, 1, 0, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums2)}")  # Expected: 2

    # Edge case: all ones
    nums3 = [1, 1, 1, 1, 1]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums3)}")  # Expected: 5

    # Edge case: all zeros
    nums4 = [0, 0, 0, 0]
    print(f"Input: {nums4}")
    print(f"Output: {solution.findMaxConsecutiveOnes(nums4)}")  # Expected: 0