n = 5

def climbStairs(n = int):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        nums = [1, 1]
        for i in range(n - 1):
            num = nums[-1] + nums[-2]
            nums.append(num)
        return nums[-1]

print(climbStairs(n))