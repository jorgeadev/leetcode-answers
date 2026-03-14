

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        # https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.java
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.cpp
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.cs
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.js
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.php
        # https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.rb

        # Generate the first permutation
        permutation = list(range(1, n + 1))

        # Generate the next k - 1 permutations
        for _ in range(k - 1):
            # Step 1: Find the largest index i such that permutation[i] < permutation[i + 1].
            # If no such index exists, the permutation is the last permutation.
            i = len(permutation) - 2
            while i >= 0 and permutation[i] >= permutation[i + 1]:
                i -= 1

            if i < 0:
                break

            # Step 2: Find the largest index j greater than i such that permutation[i] < permutation[j].
            j = len(permutation) - 1
            while permutation[i] >= permutation[j]:
                j -= 1

            # Step 3: Swap the value of permutation[i] with that of permutation[j].
            permutation[i], permutation[j] = permutation[j], permutation[i]

            # Step 4: Reverse the sequence from permutation[i + 1] up to and including the final element permutation[n].
            permutation[i + 1:] = reversed(permutation[i + 1:])

        # Convert the list of integers to a string
        return ''.join(map(str, permutation))


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n, k = 3, 3
    print(f"Input: n = {n}, k = {k}")
    print(f"Output: {solution.getPermutation(n, k)}")  # Expected: "213"

    # Example 2
    n, k = 4, 9
    print(f"Input: n = {n}, k = {k}")
    print(f"Output: {solution.getPermutation(n, k)}")  # Expected: "2314"

    # Example 3
    n, k = 3, 1
    print(f"Input: n = {n}, k = {k}")
    print(f"Output: {solution.getPermutation(n, k)}")  # Expected: "123"
