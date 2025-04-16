def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):
        current = nums[i]
        
        while stack and stack[-1] <= current:
            stack.pop()
        
        if stack:
            res[i] = stack[-1]
        
        stack.append(current)

    return res
#TIME COMPLEXITY = O(N)
#SPACE COMPLEXITY = O(N)