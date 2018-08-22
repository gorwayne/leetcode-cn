class Solution:
    def search(self, nums, target):
        min = 0
        max = len(nums) - 1

        if(target in nums):
            while True:
                center = int((min + max) / 2)
                if nums[center] > target:
                    max = center - 1
                elif nums[center] < target:
                    min = center + 1
                elif nums[center] == target:
                    print(str(target) + "在数组里面的第" + str(center) + "个位置")
                    return center
        else:
            return -1


solution = Solution()
result = solution.search([-1,0,3,5,9,12], 9)
print(result)