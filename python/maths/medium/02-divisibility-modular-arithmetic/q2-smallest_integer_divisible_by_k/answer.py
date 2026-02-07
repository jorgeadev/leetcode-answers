class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        n = 1
        length = 1
        while n % k != 0:
            n = (n * 10 + 1) % k
            length += 1
        return length


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    k1 = 1
    print(f"Input: {k1}")
    print(f"Output: {solution.smallestRepunitDivByK(k1)}")  # Expected: 1

    # Example 2
    k2 = 2
    print(f"Input: {k2}")
    print(f"Output: {solution.smallestRepunitDivByK(k2)}")  # Expected: -1

    # Example 3
    k3 = 3
    print(f"Input: {k3}")
    print(f"Output: {solution.smallestRepunitDivByK(k3)}")  # Expected: 3

    # Example 4
    k4 = 4
    print(f"Input: {k4}")
    print(f"Output: {solution.smallestRepunitDivByK(k4)}")  # Expected: -1

    # Example 5
    k5 = 5
    print(f"Input: {k5}")
    print(f"Output: {solution.smallestRepunitDivByK(k5)}")  # Expected: -1

    # Example 6
    k6 = 6
    print(f"Input: {k6}")
    print(f"Output: {solution.smallestRepunitDivByK(k6)}")  # Expected: -1

    # Example 7
    k7 = 7
    print(f"Input: {k7}")
    print(f"Output: {solution.smallestRepunitDivByK(k7)}")  # Expected: 6

    # Example 8
    k8 = 8
    print(f"Input: {k8}")
    print(f"Output: {solution.smallestRepunitDivByK(k8)}")  # Expected: -1

    # Example 9
    k9 = 9
    print(f"Input: {k9}")
    print(f"Output: {solution.smallestRepunitDivByK(k9)}")  # Expected: 9

    # Example 10
    k10 = 10
    print(f"Input: {k10}")
    print(f"Output: {solution.smallestRepunitDivByK(k10)}")  # Expected: -1
