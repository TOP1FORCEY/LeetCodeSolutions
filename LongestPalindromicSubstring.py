class Solution(object):
    def longestPalindrome(self, s = str):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        
        if s == s[::-1]:
            return s
        
        while len(s) > 1:
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    if len(output) <= len(s[:i]):
                        output = s[:i]
            s = s[1:]
                    
        return output
        
        
smtn = "babadbbabbrete"
s = Solution()
print(s.longestPalindrome(smtn))