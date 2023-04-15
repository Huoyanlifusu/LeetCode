class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        values = []
        for value in dic.values():
            if value in values:
                return False
            values.append(value)
        return True
