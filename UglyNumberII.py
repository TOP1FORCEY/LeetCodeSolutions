class Solution:
    def nthUglyNumber(self, n: int) -> int:
        u = [1]
        p2 = p3 = p5 = 0
        
        while len(u) < n:
            cand = [u[p2] * 2, u[p3] * 3, u[p5] * 5]
            u.append(min(cand))
            y = [i for i, val in enumerate(cand) if val == min(cand)]
            if 0 in y:
                p2 += 1
            if 1 in y:
                p3 += 1
            if 2 in y:
                p5 += 1
                
        return u[-1] 
            
            
            
n = 10

s = Solution()
print(s.nthUglyNumber(n))