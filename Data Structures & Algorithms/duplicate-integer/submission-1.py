class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array_size = len(nums)
        num_counter = {}
        for num in nums:
            if num not in num_counter:
                num_counter[num] = 1 + num_counter.get(num, 0)
            else:
                return True
        return False

        