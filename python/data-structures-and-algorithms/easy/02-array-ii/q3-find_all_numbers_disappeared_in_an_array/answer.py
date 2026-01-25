from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
    
        # for i in range(len(nums)):
        #     idx = abs(nums[i]) - 1
            
        #     if nums[idx] > 0:
        #         nums[idx] *= -1

        # res = []
        
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         res.append(i+1)
        
        # return res


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {solution.findDisappearedNumbers(nums1)}")  # Expected: [5, 6]

    # Example 2
    nums2 = [1, 1]
    print(f"Input: {nums2}")
    print(f"Output: {solution.findDisappearedNumbers(nums2)}")  # Expected: [2]

    # Edge case: all numbers present
    nums3 = [1, 2, 3, 4, 5]
    print(f"Input: {nums3}")
    print(f"Output: {solution.findDisappearedNumbers(nums3)}")  # Expected: []

    # Edge case: all numbers missing
    nums4 = [2, 2, 2, 2]
    print(f"Input: {nums4}")
    print(f"Output: {solution.findDisappearedNumbers(nums4)}")  # Expected: [1, 3, 4]