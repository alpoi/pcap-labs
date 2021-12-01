# Write a script to check if sudoku solutions are valid, given 9 strings of 9 numbers each (representing rows)

sample_input = ("""
    295743861
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    154938672 """)

sudoku = sample_input

def sudoku_verify():

    sudoku = sample_input

    rows = [list(row) for row in sudoku.split()]
    # print(rows)
    for row in rows:
        for num in range(9):
            if row.count(str(num + 1)) != 1:
                return ("> Uh oh! Looks like this isn't quite right!")
    return ("> Rows look good!")

print(sudoku_verify())