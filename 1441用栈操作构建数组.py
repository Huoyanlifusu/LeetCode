class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target.sort()
        i = 1
        operations = []
        while i <= min(target[-1], n):
            if i in target:
                operations.append("Push")
            else:
                operations.append("Push")
                operations.append("Pop")
            i += 1
        return operations
