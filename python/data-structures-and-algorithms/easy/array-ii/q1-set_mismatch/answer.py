from collections import Counter
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        duplicates = [item for item, count in counts.items() if count > 1]
        total = sum(nums)
        n = len(nums)
        x = int((n*(n+1))/2)
        return [duplicates[0], (duplicates[0] + (x - total))]
    
        # dup, missing = -1, -1
        
        # for i in range(1, len(nums) + 1):
        #     count = nums.count(i)
        #     if count == 2:
        #         dup = i
        #     elif count == 0:
        #         missing = i
        
        # return [dup, missing]

    

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [1, 2, 2, 4]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findErrorNums(nums1)}")  # Expected: [2, 3]

    # Example 2
    nums2 = [1, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findErrorNums(nums2)}")  # Expected: [1, 2]

    # Edge case: larger array
    nums3 = [3, 2, 3, 4, 6, 5]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findErrorNums(nums3)}")  # Expected: [3, 1]

    # Edge case: missing number at the end
    nums4 = [1, 2, 3, 4, 4]
    print(f"Input: {nums4}")
    print(f"Output: {solution.findErrorNums(nums4)}")  # Expected: [4, 5]