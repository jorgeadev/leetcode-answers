from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result
    

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [8, 1, 2, 2, 3]
    print(f"Input: {nums1}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums1)}")  # Expected: [4,0,1,1,3]

    # Example 2
    nums2 = [6, 5, 4, 8]
    print(f"Input: {nums2}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums2)}")  # Expected: [2,1,0,3]

    # Example 3
    nums3 = [7, 7, 7, 7]
    print(f"Input: {nums3}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums3)}")  # Expected: [0,0,0,0]

    # Edge case: single element
    nums4 = [10]
    print(f"Input: {nums4}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums4)}")  # Expected: [0]

    # Edge case: all elements are the same
    nums5 = [5, 5, 5, 5, 5]
    print(f"Input: {nums5}")
    print(f"Output: {solution.smallerNumbersThanCurrent(nums5)}")  # Expected: [0,0,0,0,0]