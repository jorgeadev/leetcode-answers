class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self._is_self_dividing(num):
                result.append(num)
        return result

    def _is_self_dividing(self, num: int) -> bool:
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                return False
            temp //= 10
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    left1, right1 = 1, 22
    print(f"Input: left = {left1}, right = {right1}")
    print(f"Output: {solution.selfDividingNumbers(left1, right1)}")  # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

    # Example 2
    left2, right2 = 47, 85
    print(f"Input: left = {left2}, right = {right2}")
    print(f"Output: {solution.selfDividingNumbers(left2, right2)}")  # Expected: [48, 55, 66, 77]

    # Additional test case: single number
    left3, right3 = 12, 12
    print(f"Input: left = {left3}, right = {right3}")
    print(f"Output: {solution.selfDividingNumbers(left3, right3)}")  # Expected: [12]

    # Additional test case: no self-dividing numbers
    left4, right4 = 23, 23
    print(f"Input: left = {left4}, right = {right4}")
    print(f"Output: {solution.selfDividingNumbers(left4, right4)}")  # Expected: []

    # Additional test case: range with zero
    left5, right5 = 10, 15
    print(f"Input: left = {left5}, right = {right5}")
    print(f"Output: {solution.selfDividingNumbers(left5, right5)}")  # Expected: [11, 12, 15]