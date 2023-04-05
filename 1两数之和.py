#哈希法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            if num not in dic:
                dic[num] = [index]
            else:
                dic[num].append(index)
            if target - num in dic:
                if num != target - num:
                    return [dic[target-num][0], index]
                else:
                    if len(dic[num]) == 2:
                        return [dic[num][0], dic[num][1]]
                    else:
                        continue
