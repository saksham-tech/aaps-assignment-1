from collections import defaultdict

def subarraySum(nums, k):
    hash_map = defaultdict(int)
    hash_map[0] = 1 
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        if current_sum - k in hash_map:
            count += hash_map[current_sum - k]
        hash_map[current_sum] += 1

    return count
#TIME COMPLEXITY = O(N)
#SPACE COMPLEXITY = O(N)