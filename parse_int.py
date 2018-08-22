class Solution:

    def myAtoi(self, str):
        return_numbers = ''
        for_level = 1
        is_join = 0
        str = str.strip()
        for word in str:
            if(for_level == 1):
                if(word.isdigit() or word == '-' or word == '+'):
                    return_numbers = return_numbers + '' + word
                    is_join = 1
            else:
                if (is_join == 1 and word.isdigit()):
                    return_numbers = return_numbers + '' + word
                else:
                    is_join = 0
            for_level = for_level + 1
        if (return_numbers == '' or return_numbers == '-' or return_numbers == '+'):
            return 0
        if(int(return_numbers) <= -2147483648):
            return -2147483648
        if(int(return_numbers) >= 2147483647):
            return 2147483647
        return int(return_numbers)


solution = Solution()
result = solution.myAtoi("-91283472332")
print(result)