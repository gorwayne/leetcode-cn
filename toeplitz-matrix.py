class Solution:
    def isToeplitzMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        for i in list(range(n-1)):
            for j in list(range(m-1)):
                print(i, j)
                #print(i)
                if(matrix[i][j] != matrix[i+1][j+1]):
                    return False
        return True

solution = Solution()
result = solution.isToeplitzMatrix([[53,64,90,98,34],[91,53,64,90,98],[17,91,53,64,90]])
print(result)