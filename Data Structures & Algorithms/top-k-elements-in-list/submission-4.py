class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}
        frequency_items = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:
            counter_map[num] = 1 + counter_map.get(num, 0)
        
        for key, value in counter_map.items():
            frequency_items[value].append(key)
        

        for i in range(len(frequency_items)-1, 0, -1):
            for n in frequency_items[i]:
                result.append(n)
                if len(result)==k:
                    return result

        