class Solution:
    def largest(self, arr):
        maximum = arr[0]

        for num in arr:
            if num > maximum:
                maximum = num

        return maximum


# Example usage
arr = [1, 8, 7, 56, 90]
sol = Solution()
print(sol.largest(arr))
