class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        return n == 1
    

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n1 = 6
    print(f"Input: {n1}")
    print(f"Output: {solution.isUgly(n1)}")  # Expected: True

    # Example 2
    n2 = 8
    print(f"Input: {n2}")
    print(f"Output: {solution.isUgly(n2)}")  # Expected: True

    # Example 3
    n3 = 14
    print(f"Input: {n3}")
    print(f"Output: {solution.isUgly(n3)}")  # Expected: False

    # Additional test case: zero
    n4 = 0
    print(f"Input: {n4}")
    print(f"Output: {solution.isUgly(n4)}")  # Expected: False

    # Additional test case: negative number
    n5 = -5
    print(f"Input: {n5}")
    print(f"Output: {solution.isUgly(n5)}")  # Expected: False

    # Additional test case: one
    n6 = 1
    print(f"Input: {n6}")
    print(f"Output: {solution.isUgly(n6)}")  # Expected: True