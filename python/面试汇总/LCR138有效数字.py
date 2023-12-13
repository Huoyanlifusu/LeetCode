class Solution(object):
    def validNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isNumber(s):
            try: float(s)
            except: return False
            else: return True
        
        def isInt(s):
            try: int(s)
            except: return False
            else: return False if "." in s else True

        s = s.strip()
        if " " in s: return False
        elif "e" in s:
            l = s.split("e")
            if len(l) != 2:
                return False
            return True if isNumber(l[0]) and isInt(l[1]) else False
        elif "E" in s:
            l = s.split("E")
            if len(l) != 2:
                return False
            return True if isNumber(l[0]) and isNumber(l[1]) else False
        else: return True if isNumber(s) else False
