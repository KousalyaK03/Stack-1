# Explain your approach in briefly only at top of your code
# Approach:
# - Use a monotonic decreasing stack to store indices of temperatures.
# - For each day, check if the current temperature is higher than the temperature at the index on top of the stack.
# - If yes, calculate the number of days between these indices and update the result.
# - Continue this process for all temperatures, and any indices remaining in the stack will have a result of 0 since there are no warmer days for them.

# Time Complexity: O(n), where n is the length of the temperatures array. Each element is pushed and popped from the stack at most once.
# Space Complexity: O(n), for the stack used to store indices.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculate the number of days to wait for a warmer temperature.
        :param temperatures: List[int] - List of daily temperatures.
        :return: List[int] - List of days to wait for a warmer temperature.
        """
        n = len(temperatures)
        answer = [0] * n  # Initialize the answer array with 0s
        stack = []  # Monotonic decreasing stack to store indices of temperatures

        for i, temp in enumerate(temperatures):
            # Check if the current temperature is higher than the top of the stack
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()  # Index of the previous day with a lower temperature
                answer[prev_day] = i - prev_day  # Calculate the number of days
            stack.append(i)  # Push the current index onto the stack

        return answer  # Return the final answer array

# Example Usage
# sol = Solution()
# print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))  # Output: [1,1,4,2,1,1,0,0]
# print(sol.dailyTemperatures([30,40,50,60]))  # Output: [1,1,1,0]
# print(sol.dailyTemperatures([30,60,90]))  # Output: [1,1,0]
