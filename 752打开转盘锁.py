#bfs 双端队列的使用 .popleft() 集合去重妙用 多元素更新用set.update()
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def up(s, index):
            lst = list(s)
            if lst[index] == "9":
                lst[index] = "0"
            else:
                lst[index] = str(int(lst[index]) + 1)
            return "".join(lst)
        
        def down(s, index):
            lst = list(s)
            if lst[index] == "0":
                lst[index] = "9"
            else:
                lst[index] = str(int(lst[index]) - 1)
            return "".join(lst)
        
        queue = collections.deque()
        queue.append("0000")

        visited = set()
        visited.update(deadends)

        step = 0
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur == target:
                    return step
                if cur in visited:
                    continue
                else:
                    visited.add(cur)
                    for i in range(4):
                        upcode = up(cur, i)
                        if upcode not in visited:
                            queue.append(upcode)
                        downcode = down(cur, i)
                        if downcode not in visited:
                            queue.append(downcode)
            step += 1
        
        return -1
