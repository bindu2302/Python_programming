def sum_of_diagonals(matrix):
    n = len(matrix)
    primary_sum = sum(matrix[i][i] for i in range(n))
    secondary_sum = sum(matrix[i][n-i-1] for i in range(n))

    # if n%2==1:
    #     middle_ele = matrix[n//2][n//2]
    #     return primary_sum + secondary_sum - middle_ele
    return primary_sum + secondary_sum

matrix = [
    [1,2,3,4],
    [4,5,6,4],
    [7,8,9,4],
    [4,5,6,4],
]
print(sum_of_diagonals(matrix))
