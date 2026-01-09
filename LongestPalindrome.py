class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        
        for l in s:     
            letters[l] = letters.get(l, 0) + 1

        output = 0
        has_single = False

        for count in letters.values():
            output += count // 2 * 2
            if count % 2 == 1:
                has_single = True

        return output + 1 if has_single else output
        
        
        
s = "abctcccddd"

so = Solution()
print(so.longestPalindrome(s))