class Solution:
    def unionArrays(self, a, b):
        union_set = set(a) | set(b)
        return list(union_set)


# Example usage
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

sol = Solution()
print(sorted(sol.unionArrays(a, b)))
