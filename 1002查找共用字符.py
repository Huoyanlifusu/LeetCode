class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        Hashtable = [0 for _ in range(26)]

        for index, char in enumerate(words[0]):
            Hashtable[ord(char) - ord('a')] += 1
        
        for word in words[1:]:
            tmp = [0 for _ in range(26)]
            for index, char in enumerate(word):
                tmp[ord(char)-ord('a')] += 1
            
            for index in range(26):
                Hashtable[index] = min(Hashtable[index], tmp[index])
        
        ans = []

        for index, num in enumerate(Hashtable):
            while num > 0:
                ans.append(str(chr(index + ord('a'))))
                num -= 1
        
        return ans
