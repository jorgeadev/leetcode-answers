class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return original == reversed_num
    
# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    x1 = 121
    print(f"Input: {x1}")
    print(f"Output: {solution.isPalindrome(x1)}")  # Expected: True

    # Example 2
    x2 = -121
    print(f"Input: {x2}")
    print(f"Output: {solution.isPalindrome(x2)}")  # Expected: False

    # Example 3
    x3 = 10
    print(f"Input: {x3}")
    print(f"Output: {solution.isPalindrome(x3)}")  # Expected: False

    # Additional test case: single digit
    x4 = 7
    print(f"Input: {x4}")
    print(f"Output: {solution.isPalindrome(x4)}")  # Expected: True

    # Additional test case: large palindrome
    x5 = 1234321
    print(f"Input: {x5}")
    print(f"Output: {solution.isPalindrome(x5)}")  # Expected: True