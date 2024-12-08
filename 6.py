# Validate a Sudoku Solution

def validate(listn):
    for i in listn:
        if sorted(i) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    # checked all inside lists if they consist every numbers from 1 to 9 and all are different
        
    for i in range(9):
        tester1 = []
        for x in listn:
            tester1.append(x[i])
        if sorted(tester1) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    # checked columns    
        
    tester2 = []
    for i in range(9):
        tester3 = []
        for x in range(3):
            tester3.append(listn[i][x])
        tester2.append(tester3)
    # first subgrid (left side) (whole columns)

    tester4 = []
    for i in range(9):
        tester5 = []
        for x in range(3, 6):
            tester5.append(listn[i][x])
        tester4.append(tester5)
    # second subgrid (middle) (whole columns)
    
    tester6 = []
    for i in range(9):
        tester7 = []
        for x in range(6, 9):
            tester7.append(listn[i][x])
        tester6.append(tester7)
    # third subgrid (right side) (whole columns)

    res1 = []
    for i in tester2:
        res1 += i
    # convert subgrids to check later

    res2 = []
    for i in tester4:
        res2 += i
    # convert subgrids to check later

    res3 = []
    for i in tester4:
        res3 += i
    # convert subgrids to check later

    if sorted(res1) != [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]:
        return False
    elif sorted(res2) != [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]:
        return False
    elif sorted(res3) != [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]:
        return False
    else:
        return True
    # subgrid check

print(validate([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 9]])) # True

print(validate([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 7, 7] # Invalid: Two 7s in the last row
]))

print(validate([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 9, 7, 9] # Invalid: Two 9s in the lastcolumn
]))

print(validate([
[5, 3, 4, 6, 7, 8, 9, 1, 2],
[6, 7, 2, 1, 9, 5, 3, 4, 8],
[1, 9, 8, 3, 4, 2, 5, 6, 7],
[8, 5, 9, 7, 6, 1, 4, 2, 3],
[4, 2, 6, 8, 5, 3, 7, 9, 1],
[7, 1, 3, 9, 2, 4, 8, 5, 6],
[9, 6, 1, 5, 3, 7, 2, 8, 4],
[2, 8, 7, 4, 1, 9, 6, 3, 5],
[3, 4, 5, 2, 8, 6, 1, 1, 9] # Invalid: Two 1s in the bottom-right subgrid
]))

print(validate([
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]
]))

# ✔