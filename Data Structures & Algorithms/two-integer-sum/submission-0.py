class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_cache = {}
        resulting_indices = [-1,-1]

        for i in range(len(nums)):
            if nums[i] in target_cache:
                return [target_cache[nums[i]], i]
            else:
                target_cache[target-nums[i]] = i  
        return resulting_indices