#回溯超时 25/32
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def huixuan(ptx, pty, ptz):
            dxy = (ptx[0] - pty[0]) * (ptx[0] - pty[0]) + (ptx[1] - pty[1]) * (ptx[1] - pty[1])
            dxz = (ptx[0] - ptz[0]) * (ptx[0] - ptz[0]) + (ptx[1] - ptz[1]) * (ptx[1] - ptz[1])
            return dxy == dxz
        def backsearch(points, startindex, path, res):
            if len(path) == 3:
                if huixuan(path[0], path[1], path[2]):
                    res += 1
                return res
            for i in range(0, len(points)):
                if points[i] in path: 
                    continue
                path.append(points[i])
                res = backsearch(points, 0, path, res)
                path.pop()
            return res
        
        return backsearch(points, 0, [], 0)
#哈希法
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        def cald(px, py):
            return (px[0]-py[0])*(px[0]-py[0]) + (px[1]-py[1])*(px[1]-py[1])

        for i in range(n):
            dic = {}
            tmp = {}
            for j in range(n):
                if i == j: continue
                d = cald(points[i], points[j])
                if d in dic:
                    dic[d] += 1
                    tmp[d] = dic[d] * (dic[d]-1)
                else:
                    dic[d] = 1
            for value in tmp.values():
                res += value
                
        return res
