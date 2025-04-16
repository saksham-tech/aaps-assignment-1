def countLessEqual(matrix, mid, n):
    count = 0
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] <= mid:
            count += (row + 1)
            col += 1
        else:
            row -= 1
    return count

def kthSmallest(matrix, k):
    n = len(matrix)
    low = matrix[0][0]
    high = matrix[n - 1][n - 1]

    while low <= high:
        mid = (low + high) // 2
        count = countLessEqual(matrix, mid, n)
        
        if count < k:
            low = mid + 1
        else:
            high = mid - 1
    return low

#TIME COMPLEXITY = 
#SPACE COMPLEXITY =O(1)