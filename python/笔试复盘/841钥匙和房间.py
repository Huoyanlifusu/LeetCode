class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        q = [0]
        visited = [0] * n
        while q:
            key = q.pop(0)
            for new_key in rooms[key]:
                if visited[new_key] == 0:
                    q.append(new_key)
            visited[key] = 1
        
        return visited == [1] * n