class Solution(object):
    def findTheDifference(self, s = str, t = str):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = list(s)
        lt = list(t)

        for l in lt:
            if l not in ls:
                return l
            else:
                ls.remove(l)
        
        
        
s = "abcd"
t = "eabcd"

so = Solution()
print(so.findTheDifference(s, t))