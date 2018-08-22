class Solution:
    def selfDividingNumbers(self, left, right):
        result = []
        for i in range(left, right+1):
            if(self.isDevidedNumbers(i) is True and i != None):
                result.append(i)
        return result

    def isDevidedNumbers(self, num):
        for i in str(num):
            if(i == '0'):
                return False
            if(num % int(i) != 0):
                return False
        return True
solution = Solution()
result = solution.selfDividingNumbers(1, 22)
print(result)