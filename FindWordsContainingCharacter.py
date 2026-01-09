class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        output = []
        
        for pos, word in enumerate(words):
            if x in word:
                output.append(pos)
        return output

words = ["leet","code"]
x = "e"

s = Solution()
print(s.findWordsContaining(words, x))