class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Convert list to tuple so it can be a dictionary key
            key = tuple(count)
            res[key].append(s)
        return list(res.values())