from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        
        for i in range(2, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i - 1] != sorted_arr[1] - sorted_arr[0]:
                return False
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    arr1 = [3, 5, 1]
    print(f"Input: {arr1}")
    print("Can make arithmetic progression:", solution.canMakeArithmeticProgression(arr1))  # Expected: True
    
    # Example 2
    arr2 = [1, 2, 4]
    print(f"Input: {arr2}")
    print("Can make arithmetic progression:", solution.canMakeArithmeticProgression(arr2))  # Expected: False

    # Additional test case 1
    arr3 = [7, 3, 5, 1]
    print(f"Input: {arr3}")
    print("Can make arithmetic progression:", solution.canMakeArithmeticProgression(arr3))  # Expected: True

    # Additional test case 2
    arr4 = [10, 20, 30, 50]
    print(f"Input: {arr4}")
    print("Can make arithmetic progression:", solution.canMakeArithmeticProgression(arr4))  # Expected: False

    # Additional test case 3
    arr5 = [5, 5, 5, 5]
    print(f"Input: {arr5}")
    print("Can make arithmetic progression:", solution.canMakeArithmeticProgression(arr5))  # Expected: True