class Solution(object):
    def lengthOfLongestSubstring(self, s = str):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            print(seen, s[right])
            while s[right] in seen:
                # Keep shrinking window from left until duplicate is removed
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length

string = "aababcabcbb"
s = Solution()
print(s.lengthOfLongestSubstring(string))