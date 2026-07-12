class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i


# Example usage
nums = [2,8,21,78.13]
target = 9

solution = Solution()
print(solution.twoSum(nums, target))