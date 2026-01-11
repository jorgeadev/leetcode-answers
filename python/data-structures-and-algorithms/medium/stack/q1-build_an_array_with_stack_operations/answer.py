from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        current = 1

        for number in target:
            while current < number:
                result.append("Push")
                result.append("Pop")
                current += 1
            result.append("Push")
            current += 1

        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    target1 = [1, 3]
    n1 = 3
    print(f"Input: target = {target1}, n = {n1}")
    print(f"Output: {solution.buildArray(target1, n1)}")  # Expected: ["Push", "Push", "Pop", "Push"]

    # Example 2
    target2 = [1, 2, 3]
    n2 = 3
    print(f"Input: target = {target2}, n = {n2}")
    print(f"Output: {solution.buildArray(target2, n2)}")  # Expected: ["Push", "Push", "Push"]

    # Example 3
    target3 = [2, 3, 4]
    n3 = 4
    print(f"Input: target = {target3}, n = {n3}")
    print(f"Output: {solution.buildArray(target3, n3)}")  # Expected: ["Push", "Pop", "Push", "Push", "Push"]

    # Edge case: single element
    target4 = [1]
    n4 = 1
    print(f"Input: target = {target4}, n = {n4}")
    print(f"Output: {solution.buildArray(target4, n4)}")  # Expected: ["Push"]

    # Edge case: skipping multiple numbers
    target5 = [2, 4, 6]
    n5 = 6
    print(f"Input: target = {target5}, n = {n5}")
    print(f"Output: {solution.buildArray(target5, n5)}")  
    # Expected: ['Push', 'Pop', 'Push', 'Push', 'Pop', 'Push', 'Push', 'Pop', 'Push']