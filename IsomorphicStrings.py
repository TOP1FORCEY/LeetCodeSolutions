class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
            
        letmap = {}      # maps s[i] -> t[i]
        reverse_map = {} # maps t[i] -> s[i]

        for i in range(len(s)):
            if s[i] in letmap:
                if letmap[s[i]] != t[i]:
                    return False
            else:
                letmap[s[i]] = t[i]
                
            if t[i] in reverse_map:
                if reverse_map[t[i]] != s[i]:
                    return False
            else:
                reverse_map[t[i]] = s[i]
        
        return True


str1 = "badc"
str2 = "baba"

s = Solution()
print(s.isIsomorphic(str1, str2))