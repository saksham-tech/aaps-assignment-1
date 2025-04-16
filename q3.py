def can_split_equal_sum(arr):
    total = sum(arr)
    left_sum = 0
    for num in arr:
        left_sum += num
        if left_sum == total - left_sum:
            return True
    return False
#TIME COMPLEXITY = O(N)
#SPACE COMPLEXITY = O(1)