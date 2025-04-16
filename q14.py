def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

#TIME COMPLEXITY = O(N)
#SPACE COMPLEXITY =O(1)