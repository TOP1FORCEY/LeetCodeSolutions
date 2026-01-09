class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arr = []
        xor = 0
        
        for i in range(n):
            arr.append(start + 2 * i)
        
        for num in arr:
            xor ^= num
        
        return xor
        
        
        
        
s = Solution()
n = 5
start = 0

print(s.xorOperation(n, start))