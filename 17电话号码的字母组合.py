class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []

        dic = {
            '2' : ["a","b","c"],
            '3' : ["d","e","f"],
            '4' : ["g","h","i"],
            '5' : ["j","k","l"],
            '6' : ["m","n","o"],
            '7' : ["p","q","r","s"],
            '8' : ["t","u","v"],
            '9' : ["w","x","y","z"]
        }

        res =[]

        def backsearch(combination, nextdigit):
            if len(nextdigit) == 0:
                res.append(combination)
            
            else:
                for letter in dic[nextdigit[0]]:
                    backsearch(combination + letter, nextdigit[1:])
        
        backsearch("", digits)
        return res
