def createPrefixSum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
        
    return prefix

def rangeSum(prefix, L, R):
    if L == 0:
        return prefix[R]
    else:
        return prefix[R] - prefix[L-1]
#TIME COMPLEXITY O(N)
#SPACE COMPLEXITY 0(N)