class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        array = []
        def backsearch(s, startIndex):
            if startIndex == len(s) and len(path) == 4:
                array.append(".".join(path.copy()))
                return
            for i in range(startIndex ,len(s)):
                ipstr = s[startIndex:i+1]
                if ipstr[0] == "0" and len(ipstr) > 1: continue
                if len(s[i+1:len(s)]) > (3-len(path))*3: continue
                ip = int(ipstr)
                if ip > 255: break
                path.append(ipstr)
                backsearch(s, i+1)
                path.pop()

        backsearch(s, 0)
        return array
