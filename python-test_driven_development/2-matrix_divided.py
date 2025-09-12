"""
Module Matrix divided

Functions:
    matrix_divided(matrix, div)
"""
#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    divide all elements of a matrix
    matrix must be a list of lists of integers or floats
    each rows of the matrix must have the same size
    div must be a number (integer or float) and can't be equal to 0
    return a new matrix, else TypeError or ZeroDivisionError
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)) or div == float("inf"):
        raise TypeError("div must be a number")
    
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    try:
        new_mat = []
        for i in matrix:
            new_mat.append(list(map(lambda x: (x / div).__round__(2), i)))
        return new_mat
    except (TypeError, ValueError) as e:
        if e == TypeError:
            raise TypeError("matrix must be a matrix (list of lists) of " \
            "integers/floats")
        else:
            raise TypeError("matrix must be a matrix (list of lists) of " \
            "integers/floats")
