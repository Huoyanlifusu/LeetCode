import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[str]
        """
        word_Dict = collections.defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                word_Dict[word[:i]+"*"+word[i+1:]].add(word)

        res = []
        def dfs(curWord, steps, sets):
            if res:
                return
            if curWord == endWord:
                res.append(steps)
                return
            for i in range(len(curWord)):
                for word in word_Dict[curWord[:i]+"*"+curWord[i+1:]]:
                    if word not in sets:
                        sets.add(word)
                        dfs(word, steps + [word], sets)
                        sets.remove(word)
        dfs(beginWord, [beginWord], {beginWord})
        return res[0] if res else res