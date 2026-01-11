from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Use int() to truncate towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tokens1 = ["2", "1", "+", "3", "*"]
    print(f"Input: {tokens1}")
    print(f"Output: {solution.evalRPN(tokens1)}")  # Expected: 9

    # Example 2
    tokens2 = ["4", "13", "5", "/", "+"]
    print(f"Input: {tokens2}")
    print(f"Output: {solution.evalRPN(tokens2)}")  # Expected: 6

    # Example 3
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(f"Input: {tokens3}")
    print(f"Output: {solution.evalRPN(tokens3)}")  # Expected: 22

    # Edge case: single number
    tokens4 = ["42"]
    print(f"Input: {tokens4}")
    print(f"Output: {solution.evalRPN(tokens4)}")  # Expected: 42

    # Edge case: negative numbers
    tokens5 = ["-4", "2", "/"]
    print(f"Input: {tokens5}")
    print(f"Output: {solution.evalRPN(tokens5)}")  # Expected: -2