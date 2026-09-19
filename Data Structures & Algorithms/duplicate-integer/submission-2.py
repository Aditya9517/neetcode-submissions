class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_cache = set()
        for num in nums:
            if num not in seen_cache:
                seen_cache.add(num)
            else:
                return True
        return False