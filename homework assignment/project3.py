class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k - 1]


# Example usage
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4
sol = Solution()
print(sol.kthSmallest(arr, k))
