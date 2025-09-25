class Solution(object):
    def lengthOfLongestSubstring(self, s = str):
        """
        :type s: str
        :rtype: int
        """
        distance = []
        
        for p, i in enumerate(s):
            seen = []
            for p2, i2 in enumerate(s):             
                print(p,i, p2,i2)
                if p <= p2:
                    if i2 in seen:
                        distance.append(p2 - p)
                        break
                    else:
                        seen.append(i2)
            else:
                distance.append(len(s) - p)
            
            
        if distance:
            return max(distance)
        return len(s)
        
        
string = "aababcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(string))