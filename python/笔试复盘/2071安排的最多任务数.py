from sortedcontainers import SortedList
class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        
        m, n = len(tasks), len(workers)

        tasks.sort(), workers.sort()


        def check(mid):
            p = pills
            ws = SortedList(workers[n-mid:])

            for i in range(mid-1, -1, -1):
                if tasks[i] <= ws[-1]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    # 可以理解成为 tasks[i]-strength 这个新元素能排到数组的第几位

                    rep = ws.bisect_left(tasks[i]-strength)
                    # print(ws, rep, tasks[i]-strength)
                    
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            
            return True

        start, end, ans = 1, min(m, n), 0
        while start <= end:
            mid = (start + end) // 2
            if check(mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        
        return ans