turn = 0

def sudoku_print():
    for i in range(9):
        for j in range(9):
            print(sudoku[(i,j)]["value"][0],end="")
        print()

#Returns all the cells in the same row as (i,j) (excluding it)
def row(i,j):
    return [(i,l) for l in range(9) if not l == j]

#Returns all the cells in the same column as (i,j) (excluding it)
def col(i,j):
    return [(k,j) for k in range(9) if not k == i]

#Returns all then cells in the same block as (i,j) (excluding cells above)
def block(i,j):
    return [(k + i//3,l + j//3) for k in range(3)
                                for l in range(3)
                                if not (k == i%3 or l == j%3)]

def neighbors(i,j):
    return row(i,j) + col(i,j) + block(i,j)

def set(cell, value):
    global sudoku
    cell["value"] = (value, turn)
    for coord in cell["neighbors"]:
        if value in sudoku[coord]["possibilities"].keys():
            del sudoku[coord]["possibilities"][value]
        if len(sudoku[coord]["possibilities"]) == 1:
            v = list(sudoku[coord]["possibilities"].keys())[0]
            del sudoku[coord]["possibilities"][v]
            set(sudoku[coord], v)

#1 Read the Sudoku puzzle
sudoku = {}
initial_cells = []
i = 0
file = open("easy1.txt","r")
for line in file:
    values = list(map(int,line.split()))
    for j in range(9):
        sudoku[(i,j)] = {
            "value":(values[j],turn),
            "possibilities":{1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None},
            "neighbors":neighbors(i,j)
        }
        if not sudoku[(i,j)]["value"] == 0: initial_cells.append((i,j))
    i += 1

sudoku_print()

#Initialize the sudoku with the initial values
for coord in initial_cells:
    set(sudoku[coord],sudoku[coord]["value"][0])

sudoku_print()