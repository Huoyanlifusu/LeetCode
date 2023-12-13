# startswith方法 + 排序
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary.sort(key = lambda x: len(x))
        sentence = sentence.split(" ")

        for i, word in enumerate(sentence):
            for root in dictionary:
                if word.startswith(root):
                    sentence[i] = root
                    break
        
        return " ".join(sentence)