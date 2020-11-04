# DEMO
# Take in a 2d list and return the sum of all values in that list.
def sum_all(table):
    total = 0
    for row in table:
        for item in row:
            total += item
    return total


# DEMO
# Take in an int n, and return an n-by-n 2d list of zeros.
def zeros_2d(n):
    result = []
    for i in range(n):
        result.append([])
        for j in range(n):
            result[i].append(0)
    return result


# Take in a 2d list, and return the sum of the elements along the upper-left-to-lower-right diagonal.
# The matrix is guaranteed to be square. (The width and height will be equal).
# diagonal_sum([[1, 2, 3]
#               [4, 5, 6], 
#               [7, 8, 9]]) returns 15 (1 + 5 + 9)
# diagonal_sum([[1, 0, 0, 0], 
#               [0, 1, 0, 0], 
#               [0, 0, 1, 0], 
#               [0, 0, 0, 1]]) returns 4 (1 + 1 + 1 + 1)
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total
print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Take in a 2d list, and return the sum of the elements on both diagonals.
# If there's a center element, make sure to only include it once!
# The matrix is guaranteed to be square.
# x_sum([[1, 2, 3], 
#        [4, 5, 6], 
#        [7, 8, 9]]) returns 25 (1 + 5 + 9 + 3 + 7)
# x_sum([[1, 0, 0, 2], [0, 1, 2, 0], [0, 2, 1, 0], [2, 0, 0, 1]]) returns 12 (1 + 1 + 1 + 1 + 2 + 2 + 2 + 2)
def x_sum(matrix):
    left_diagonal_sum = 0
    right_diagonal_sum = 0
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    for i in range(len(matrix)):
        left_diagonal_sum += matrix[i][i]
        j = (len(matrix) - i - 1)
        if j != i:
            right_diagonal_sum += matrix[i][j]
    return left_diagonal_sum + right_diagonal_sum



# Take in a 2-dimensional list of ints, and return the maximum int in the structure.
# All of the values are guaranteed to be ints above 0. The input is guaranteed to be non-empty.
# The input is guaranteed to be rectangular, this means
# no row will be shorter or longer than any other, but it is not guaranteed to be square.
# max_2d([[1, 2, 3], [4, 5, 4], [3, 2, 1]]) returns 5
# max_2d([[1, 6], [2, 3]]) returns 6
def max_2d(values):
    result = []
    for i in range(len(values)):
        result.append(max(values[i]))
    return max(result)

# print(max_2d([[1, 2, 3], [4, 5, 4], [3, 2, 1]]))

# Take in a 2-dimensional list of ints, and return the coordinates [row, col] of the maximum value.
# All of the values are guaranteed to be ints above 0.
# The input is guaranteed to be rectangular and not empty.
# max_2d_index([[1, 2, 3], [4, 5, 4], [3, 2, 1]]) returns [1, 1] (the indexes of the value 5)
# max_2d_index([[1, 6], [2, 3]]) returns [0, 1] (the indexes of the value 6)
def max_2d_index(values):
    max_val = 0
    for i in range(len(values)):
        for j in range(len(values[0])):
            if values[i][j] > max_val:
                max_index = [i,j]
                max_val = values[i][j]
    return max_index
print(max_2d_index([[1, 2, 3], [4, 5, 4], [3, 2, 1]]))


# Take in an integer n, and return a 2d list containing the "times table" from 1*1 up to n*n.
# n is guaranteed to be greater than 0.
# If you're not familiar with "times tables", an example can be found at mathsisfun.com/tables
# times_table(1) returns [[1]]
# times_table(2) returns [[1, 2], [2, 4]]
# times_table(3) returns [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
def times_table(n):
    start_val = []
    for i in range(n):
        start_val.append([])
        for j in range(n):
            start_val[i].append(j+1)
            start_val[i][j] = start_val[i][j] * (i+1)
    return start_val
result = times_table(12)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in result]))

# Take in a 2-dimensional list, and return that same list with the rows and columns switched.
# The input is guaranteed to be rectangular and not empty.
# transpose([[1, 2, 3], 
#            [4, 5, 6]]) returns [
# [1, 4], 
# [2, 5], 
# [3, 6]]
def transpose(matrix):
    num_cols = len(matrix)
    num_rows = len(matrix[0])
    result = []
    for i in range(num_rows):
        result.append([])
        for j in range(num_cols):
            result[i].append(matrix[j][i])
    return result

result = transpose([[1, 2, 3], [4, 5, 6]])
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in result]))
