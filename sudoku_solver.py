verb = False

turn = 0
pointer = (0,0)

def sudoku_print():
    print("----------------------")
    for i in range(9):
        print("|", end="")
        for j in range(9):
            print(sudoku[(i,j)][0],
                 ("*" if (i,j) == pointer else " "),
                 ("|" if j%3 == 2 else ""),
                 end="", sep="")
        print()
        if i%3 == 2: print("----------------------")

def neighbors(i,j): # neighbors include (i,j)
    return [(k,l) for k in range(9) for l in range(9) if
            (k == i or l == j or (k//3 == i//3 and l//3 == j//3))]

def set(coord, value):
    global sudoku, pointer
    sudoku[coord] = [value,[]]
    for ij in neighbors(*coord):
        if value in sudoku[ij][1]: sudoku[ij][1].remove(value)
        if len(sudoku[ij][1]) == 1: set(ij, *sudoku[ij][1])

import time
start = time.time()

#2 Initialise empty sudoku
sudoku = {}
for coord in [(i,j) for i in range(9) for j in range(9)]:
    sudoku[coord] = [0,list(range(1,10))]

i = 0
file = open("easy1.txt","r")
for line in file:
    for x in enumerate(list(map(int,line.split()))):
        if x[1] != 0: set((i,x[0]),x[1])
    i += 1

print("Initialisation in :",time.time()-start,"seconds")
sudoku_print()


# for coord in [(i,j) for i in range(9) for j in range(9) if sudoku[(i,j)] == 0]:
#     set(coord,sudoku[coord][1].pop(),[])

# for coord, cell in sudoku.items(): print(len(cell["possibilities"]))

