class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lists = []
        for a in s:
            lists.append(a)
        lists.sort()
        
        listt = []
        for a in t:
            listt.append(a)
        listt.sort()
        
        print(listt, lists)
        
        return lists == listt
    
s = "anagram"
t = "nagaram"

a = Solution()
print(a.isAnagram(s,t))