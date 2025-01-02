# Explain your approach in briefly only at top of your code
# Approach:
# - To handle the circular nature of the array, simulate a doubled array by iterating through `nums` twice.
# - Use a monotonic decreasing stack to keep track of indices where the next greater element hasn't been found yet.
# - For each element, if it is greater than the element at the index stored on the top of the stack, update the result.
# - If no greater element exists for an index after both iterations, set its value to -1.

# Time Complexity: O(n), where n is the length of the nums array. Each element is pushed and popped from the stack at most once.
# Space Complexity: O(n), for the stack used to store indices and the result array.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Find the next greater element for each element in a circular array.
        :param nums: List[int] - Input circular array.
        :return: List[int] - List of next greater elements or -1 if not found.
        """
        n = len(nums)
        answer = [-1] * n  # Initialize the result array with -1
        stack = []  # Monotonic decreasing stack to store indices

        # Iterate through the array twice to simulate circular behavior
        for i in range(2 * n):
            current_index = i % n  # Simulate circular indexing
            current_value = nums[current_index]

            # Update the next greater element for indices in the stack
            while stack and nums[stack[-1]] < current_value:
                prev_index = stack.pop()
                answer[prev_index] = current_value
            
            # Only push indices from the first pass into the stack
            if i < n:
                stack.append(current_index)
        
        return answer  # Return the final result array

# Example Usage
# sol = Solution()
# print(sol.nextGreaterElements([1, 2, 1]))  # Output: [2, -1, 2]
# print(sol.nextGreaterElements([1, 2, 3, 4, 3]))  # Output: [2, 3, 4, -1, 4]
