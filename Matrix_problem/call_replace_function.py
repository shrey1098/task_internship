from Matrix_problem import main

# initial array or matrix
arr = [["a", "b", 1, "d", 1, "f"],
       ["b", "c", "d", "e", "f", "a"],
       [2, "d", "e", "f", "a", "b"],
       ["d", "e", "f", "a", "b", "c"],
       ["e", "f", "a", 3, "c", "d"],
       ["f", "a", "b", "c", "d", "e"]]

print(main.replace_int(matrix=arr))