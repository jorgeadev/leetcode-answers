from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])
        return res
    

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [2,5,1,3,4,7]
    n1 = 3
    print(f"Input: nums = {nums1}, n = {n1}")
    print(f"Output: {solution.shuffle(nums1, n1)}")  # Expected: [2,3,5,4,1,7]

    # Example 2
    nums2 = [1,2,3,4,4,3,2,1]
    n2 = 4
    print(f"Input: nums = {nums2}, n = {n2}")
    print(f"Output: {solution.shuffle(nums2, n2)}")  # Expected: [1,4,2,3,3,2,4,1]

    # Example 3
    nums3 = [1,1,2,2]
    n3 = 2
    print(f"Input: nums = {nums3}, n = {n3}")
    print(f"Output: {solution.shuffle(nums3, n3)}")  # Expected: [1,2,1,2]