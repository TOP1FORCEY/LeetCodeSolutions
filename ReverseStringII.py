class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # Convert string to list for easier manipulation
        s_list = list(s)
        n = len(s_list)
        
        # Process every 2k characters
        for i in range(0, n, 2 * k):
            # Determine the end index for reversal
            # We want to reverse at most k characters starting from i
            end = min(i + k - 1, n - 1)
            
            # Reverse the substring from i to end
            left, right = i, end
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        
        return ''.join(s_list)
        
        
sol = Solution()
s = "abcdefg"
k = 2
print(sol.reverseStr(s,k))