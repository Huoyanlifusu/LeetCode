class Solution:
    def simplifyPath(self, path: str) -> str:
        path += "/"
        tmpstr = ""
        res = []
        for index, char in enumerate(path):
            if char == "/":
                if tmpstr and tmpstr == ".":
                    res = res
                elif tmpstr and tmpstr == "..":
                    if res:
                        res.pop()
                elif tmpstr:
                    res.append(tmpstr)
                tmpstr = ""
            else:
                tmpstr += char
        
        return "/" + "/".join(res)
