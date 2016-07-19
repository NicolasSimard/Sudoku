# To test: python -m cProfile solver.py

def print_neigh(n):
    for row in range(9):
        for col in range(9*row,9*row+9):
            print("*" if col in nlist[n] else "-",end = " ")
        print()
    print()
  
def neigh(n,sudoku):
    return [sudoku[i] for i in range(81) if (n%9 == i%9 or n//9 == i//9 or (n//27 == i//27 and (n//3)%3 == (i//3)%3)) and n != i]
    
def print_sudoku(sudoku):
    for row in range(9):
        for col in range(9*row,9*row+9):
            print(sudoku[col],end = " ")
        print()
    print()

# def neigh(n,sudoku):
    # return [sudoku[(n+9*i)%81] for i in range(9)]+\
           # [sudoku[9*(n//9)+i] for i in range(9)]+\
           # [sudoku[27*(n//27)+9*i+3*((n//3)%3)+j] for i in range(3) for j in range(3)]
           
sudoku = []
file = open("hardest1.txt","r")
for line in file:
    sudoku += list(map(int,line.split()))
print_sudoku(sudoku)  


nlist = [neigh(n,range(81)) for n in range(81)]    
guess = []
n,i = 0,1
while 1:
    while n < 81 and sudoku[n] != 0: n+=1
    if n == 81: break
    L = [sudoku[i] for i in nlist[n]]
    #L = neigh(n,sudoku)
    while i <= 9 and i in L: i+=1
    if i <= 9:
        guess += [(n,i)]
        sudoku[n] = i
        i = 1
    else:
        n,i = guess.pop()
        sudoku[n] = 0
        i += 1
    
print_sudoku(sudoku)

