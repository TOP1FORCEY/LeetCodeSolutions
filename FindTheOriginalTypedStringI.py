class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        output = 1
        n = len(word)
        i = 0
        
        while i < n:
            j = i
            
            while j < n and word[j] == word[i]:
                j += 1
            
            output += (j - i - 1)
            
            i = j
            
        return output
        
        
word = "abbcccc"

s = Solution()
print(s.possibleStringCount(word))