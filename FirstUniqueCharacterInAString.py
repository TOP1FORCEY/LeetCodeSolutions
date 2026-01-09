class Solution(object):
    def firstUniqChar(self, s = str):
        """
        :type s: str
        :rtype: int
        """
        symbols = {}
        
        for symb in s:
            if symb not in symbols:
                symbols[symb] = 1
            else:
                symbols[symb] += 1
        
        for char in symbols.items():
            if char[1] == 1:
                return s.find(char[0])
            
        return -1
    
s = "leetcode"

so = Solution()
print(so.firstUniqChar(s))