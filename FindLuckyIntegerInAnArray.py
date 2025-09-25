class Solution(object):
    def findLucky(self, arr = list):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        
        values = set(arr)
        
        table = {}
         
        for value in values:
            b = 0
            for a in arr:
                if value == a:
                    b += 1
            table[value] = b
        
        output = []
        
        for a in table:
            if table[a] == a:
                output.append(a)
        
        return max(output) if output else -1
        
        
        
arr = [2,2,3,4,4]
s = Solution()
print(s.findLucky(arr))