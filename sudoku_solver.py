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

def neighbors(i,j): # neighbors does not include (i,j)
    L = [(k,l) for k in range(9) for l in range(9) if
            (k == i or l == j or (k//3 == i//3 and l//3 == j//3))]
    L.remove((i,j))
    return L


def guess(coord, value, hist):
    global sudoku
    sudoku[coord][0] = value
    sudoku[ij][1].remove(value)
    hist.append((coord, value)) # means tried value value at cell coord
    for ij in neighbors(*coord):
        if value in sudoku[ij][1]:
            sudoku[ij][1].remove(value)
            hist.append((ij, -value)) # means removed possibility value from cell ij
            if len(sudoku[ij][1]) == 0:
                break
            if len(sudoku[ij][1]) == 1:
                guess(ij, sudoku[ij][1], hist)

def set(coord, value):
    global sudoku
    sudoku[coord] = [value,[]]
    for ij in neighbors(*coord):
        if value in sudoku[ij][1]:
            sudoku[ij][1].remove(value)
    for ij in neighbors(*coord):
        if len(sudoku[ij][1]) == 0 and sudoku[ij][0] == 0: # We have a contradiction
            return False
        if len(sudoku[ij][1]) == 1: # This cell is determined
            return set(ij, sudoku[ij][1][0])
    return True

import time
start = time.time()

#1 Initialise empty sudoku
sudoku = {}
for coord in [(i,j) for i in range(9) for j in range(9)]:
    sudoku[coord] = [0,list(range(1,10))]

#2 Initializing sudoku
i = 0
file = open("easy1.txt","r")
for line in file:
    for x in enumerate(list(map(int,line.split()))):
        if x[1] != 0: set((i,x[0]),x[1])
    i += 1

print("Initialisation in :",time.time()-start,"seconds")
sudoku_print()
for coord in [(i,j) for i in range(9) for j in range(9)]:
    print(coord,":",sudoku[coord])
k, l, N = list(map(int,input().split()))
while set((k,l),N):
    sudoku_print()
    for coord in [(i,j) for i in range(9) for j in range(9)]:
        print(coord,":",sudoku[coord])
    k, l, N = list(map(int,input().split()))

# stack = []
# pointer = (0,0)
# while 1:
#     # Find a free cell
#     while sudoku[pointer] != 0 and pointer != (0,0):
#         pointer[1] = (pointer[1] + (pointer[0] + 1)//9)%9
#         pointer[0] = (pointer[0] + 1)%9
#     if pointer == (0,0): break
#     stack.append(guess(pointer,sudoku[pointer][1].pop(),[]))
#     if len(sudoku[pointer][1]) > 0: # There is a possibility

#     else:
#         hist = stack.pop()
#         wrong_guess = hist.pop(0)
#         sudoku[wrong_guess[1]][0] = 0 #Reset the wrong cell
#         for value, coord in hist: # Undo history
#             if value < 0: sudoku[coord][1]
#     pointer[1] = (pointer[1] + (pointer[0] + 1)//9)%9
#     pointer[0] = (pointer[0] + 1)%9



# for coord in [(i,j) for i in range(9) for j in range(9) if sudoku[(i,j)] == 0]:
#     set(coord,sudoku[coord][1].pop(),[])

# for coord, cell in sudoku.items(): print(len(cell["possibilities"]))

