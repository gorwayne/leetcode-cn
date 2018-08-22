class Solution:
    def transpose(self, A):
        t_matrix = [[] for i in A[0]]
        for i in A:
            for j in range(len(i)):
                t_matrix[j].append(i[j])
        return t_matrix

solution = Solution()
result = solution.transpose([[1,2,3],[4,5,6]])
print(result)