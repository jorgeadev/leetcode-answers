from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            func_id, action, timestamp = log.split(':')
            func_id = int(func_id)
            timestamp = int(timestamp)
            
            if action == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:  # end
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        
        return result
    

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n1 = 2
    logs1 = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    print(f"Input: n = {n1}, logs = {logs1}")
    print(f"Output: {solution.exclusiveTime(n1, logs1)}")  # Expected: [3, 4]

    # Example 2
    n2 = 1
    logs2 = ["0:start:0", "0:end:0"]
    print(f"Input: n = {n2}, logs = {logs2}")
    print(f"Output: {solution.exclusiveTime(n2, logs2)}")  # Expected: [1]

    # Edge case: nested functions
    n3 = 2
    logs3 = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    print(f"Input: n = {n3}, logs = {logs3}")
    print(f"Output: {solution.exclusiveTime(n3, logs3)}")  # Expected: [7,1]