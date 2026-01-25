class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            left_sum = (i * (i + 1)) // 2
            right_sum = (n * (n + 1)) // 2 - ((i - 1) * i) // 2
            if left_sum == right_sum:
                return i
        return -1
    
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n1 = 8
    print(f"Input: {n1}")
    print(f"Output: {solution.pivotInteger(n1)}")  # Expected: 6

    # Example 2
    n2 = 1
    print(f"Input: {n2}")
    print(f"Output: {solution.pivotInteger(n2)}")  # Expected: 1

    # Additional test case: no pivot integer
    n3 = 4
    print(f"Input: {n3}")
    print(f"Output: {solution.pivotInteger(n3)}")  # Expected: -1

    # Additional test case: larger n
    n4 = 15
    print(f"Input: {n4}")
    print(f"Output: {solution.pivotInteger(n4)}")  # Expected: 9