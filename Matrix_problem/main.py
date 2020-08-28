import numpy as np

# initial array or matrix
arr = [["a", "b", 1, "d", 1, "f"],
       ["b", "c", "d", "e", "f", "a"],
       [2, "d", "e", "f", "a", "b"],
       ["d", "e", "f", "a", "b", "c"],
       ["e", "f", "a", 3, "c", "d"],
       ["f", "a", "b", "c", "d", "e"]]


# function takes the matrix as argument
def replace_int(matrix):
    # function iterates over each object in all the rows of the matrix to find out the integers 1 , 2 or 3
    for row in matrix:
        for i in row:
            # replaces 1 with the object in row 2 with the same index value as 1
            if i == 1:
                ind_row = matrix.index(row)
                ind_value = row.index(i)
                matrix[ind_row][ind_value] = matrix[1][ind_value]
            # replaces 2 with the object in row 2 with the same index value as 2
            elif i == 2:
                ind_row = matrix.index(row)
                ind_value = row.index(i)
                matrix[ind_row][ind_value] = matrix[1][ind_value]
            # replaces 3 with the sum of corner objects of the matrix
            elif i == 3:
                ind_row = matrix.index(row)
                ind_value = row.index(i)
                matrix[ind_row][ind_value] = matrix[0][0] + matrix[0][-1] + matrix[-1][0] + matrix[-1][-1]
    # returns matrix as a numpy array
    return np.array(matrix)


if __name__ == '__main__':
    print(replace_int(matrix=arr))

