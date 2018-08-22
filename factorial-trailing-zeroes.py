class Solution:
    # def trailingZeroes(self, n):
    #     fact = self.factorial(n)
    #     print(fact)


    # def factorial(self, n):
    #     if n < 2:
    #         return 1
    #     else:
    #         return n * self.factorial(n-1)
    
    def trailingZeroes(self, n):
        num = 0
        while(n):
            num = num +  n // 5
            n = n // 5
        return num

solution = Solution()
result = solution.trailingZeroes(10)
print(result)