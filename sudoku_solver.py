verb = False

turn = 0
pointer = (0,0)

def sudoku_print():
    print("----------------------")
    for i in range(9):
        print("|", end="")
        for j in range(9):
            print(sudoku[(i,j)]["value"][0],
                 ("*" if (i,j) == pointer else " "),
                 ("|" if j%3 == 2 else ""),
                 end="", sep="")
        print()
        if i%3 == 2: print("----------------------")

#Returns all the cells in the same row as (i,j) (excluding it)
def row(i,j):
    return [(i,l) for l in range(9) if not l == j]

#Returns all the cells in the same column as (i,j) (excluding it)
def col(i,j):
    return [(k,j) for k in range(9) if not k == i]

#Returns all then cells in the same block as (i,j) (excluding cells above)
def block(i,j):
    return [(k + 3*(i//3),l + 3*(j//3)) for k in range(3) for l in range(3)
                                        if not (k == i%3 or l == j%3)]

def neighbors(i,j):
    return row(i,j) + col(i,j) + block(i,j)

def set(coord, value):
    global sudoku, pointer, verb
    if verb:
        pointer = coord
        print("Setting cell",sudoku[coord]["coord"],"to",value)
        print("Number of possibilities:",len(sudoku[coord]["possibilities"]))
    sudoku[coord]["value"] = (value, turn)
    sudoku[coord]["possibilities"] = {}
    for ij in sudoku[coord]["neighbors"]:
        if verb:
            pointer = ij
            sudoku_print()
            input()
        if value in sudoku[ij]["possibilities"].keys():
            del sudoku[ij]["possibilities"][value]
        if len(sudoku[ij]["possibilities"]) == 1:
            v = list(sudoku[ij]["possibilities"].keys())[0]
            set(ij, v)


#1 Read the Sudoku puzzle
sudoku = {}
initial_coord = []
i = 0
file = open("easy1.txt","r")
for line in file:
    values = list(map(int,line.split()))
    for j in range(9):
        sudoku[(i,j)] = {
            "coord":(i,j),
            "value":(values[j],turn),
            "possibilities":{1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None},
            "neighbors":neighbors(i,j)
        }
        if sudoku[(i,j)]["value"][0] != 0: initial_coord.append((i,j))
    i += 1

sudoku_print()

#Initialize the sudoku with the initial values
for coord in initial_coord:
    if verb: print("In init loop with cell",coord)
    set(coord,sudoku[coord]["value"][0])

sudoku_print()

if verb:
    for coord, cell in sudoku.items(): print(len(cell["neighbors"]))

