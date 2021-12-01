# LAB only required checking rows, here's the whole thing

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

def sudoku_verify(sudoku, helpful = False): # helpful options points the player to where the mistake was made
    
    rows = [list(row) for row in sudoku.split()]

    for row in rows:
        for num in range(9):
            if row.count(str(num + 1)) != 1:
                if helpful:
                    return ("> Uh oh! Looks like there's a problem on row", str(num + 1) + "!")
                else:
                    return ("> Uh oh! Looks like this isn't right!")
    print("> Rows look good!")

    cols = [[row[i] for row in rows] for i in range(9)]
    
    for col in cols:
        for num in range(9):
            if col.count(str(num + 1)) != 1:
                if helpful:
                    return ("> Uh oh! Looks like there's a problem on column", str(num + 1) + "!")
                else:
                    return ("> Uh oh! Looks like this isn't right!")
    print("> Columns look great!")
    
    blocks = [[] for i in range(9)] # there may be a faster way to do this but I never found it...
    blocks[0] = [rows[i][j] for i in range(3) for j in range(3)]
    blocks[1] = [rows[i + 3][j] for i in range(3) for j in range(3)]
    blocks[2] = [rows[i + 6][j] for i in range(3) for j in range(3)]
    blocks[3] = [rows[i][j + 3] for i in range(3) for j in range(3)]
    blocks[4] = [rows[i + 3][j + 3] for i in range(3) for j in range(3)]
    blocks[5] = [rows[i + 6][j + 3] for i in range(3) for j in range(3)]
    blocks[6] = [rows[i][j + 6] for i in range(3) for j in range(3)]
    blocks[7] = [rows[i + 3][j + 6] for i in range(3) for j in range(3)]
    blocks[8] = [rows[i + 6][j + 6] for i in range(3) for j in range(3)]

    for block in blocks:
        for num in range(9):
            if block.count(str(num + 1)) != 1:
                if helpful:
                    return ("> Uh oh! Looks like there's a problem in block", str(num + 1) + "!")
                else:
                    return ("> Uh oh! Looks like this isn't right!")
    print("> Blocks look fantastic!")
    return ("> Congratulations! That's one fine looking sudoku!")


print(sudoku_verify(sample_input))