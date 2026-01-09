class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        
        ns = {}
        for n in nums:
            if n in ns:
                ns[n] += 1
            else:
                ns[n] = 1    
        
        maxn = max(ns.values())
        candidates = [num for num in ns if ns[num] == maxn]
        
        solution = []
        
        for candidate in candidates:
            copy_nums = nums.copy()
            start_i = 0
            end_i = len(nums) - 1

            while start_i < len(nums) and end_i >= start_i:
                if copy_nums[start_i] != candidate:
                    start_i += 1
                else:
                    if copy_nums[end_i] != candidate:
                        end_i -= 1
                    else:
                        solution.append(end_i - start_i)
                        break
                    
        return min(solution) + 1
        
    
nums = [2,1]

s = Solution()
print(s.findShortestSubArray(nums))