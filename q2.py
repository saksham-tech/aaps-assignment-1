def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == total - left_sum - arr[i]:
            return i
        left_sum += arr[i]
    return -1

#TIME COMPLEXITY = O(N)
#SPACE COMPLEXITY = O(1)