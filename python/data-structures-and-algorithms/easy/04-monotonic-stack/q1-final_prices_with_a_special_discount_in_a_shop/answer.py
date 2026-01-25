from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    prices1 = [8, 4, 6, 2, 3]
    print(f"Input: {prices1}")
    print(f"Output: {solution.finalPrices(prices1)}")  # Expected: [4, 2, 4, 2, 3]

    # Example 2
    prices2 = [1, 2, 3, 4, 5]
    print(f"Input: {prices2}")
    print(f"Output: {solution.finalPrices(prices2)}")  # Expected: [1, 2, 3, 4, 5]

    # Edge case: all prices have discounts
    prices3 = [10, 1, 1, 1, 1]
    print(f"Input: {prices3}")
    print(f"Output: {solution.finalPrices(prices3)}")  # Expected: [9, 0, 0, 0, 1]