from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        anwsers = [0] * len(temperatures)
        stack = []  # This will store indices of the temperatures list

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                anwsers[index] = i - index
            stack.append(i)
        return anwsers


        # answers = [0] * len(temperatures)
        
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             answers[i] = j - i
        #             break
        # return answers    


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Input: {temperatures1}")
    print(f"Output: {solution.dailyTemperatures(temperatures1)}")  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]

    # Example 2
    temperatures2 = [30, 40, 50, 60]
    print(f"Input: {temperatures2}")
    print(f"Output: {solution.dailyTemperatures(temperatures2)}")  # Expected: [1, 1, 1, 0]

    # Example 3
    temperatures3 = [30, 60, 90]
    print(f"Input: {temperatures3}")
    print(f"Output: {solution.dailyTemperatures(temperatures3)}")  # Expected: [1, 1, 0]

    # Edge case: all same temperatures
    temperatures4 = [50, 50, 50]
    print(f"Input: {temperatures4}")
    print(f"Output: {solution.dailyTemperatures(temperatures4)}")  # Expected: [0, 0, 0]