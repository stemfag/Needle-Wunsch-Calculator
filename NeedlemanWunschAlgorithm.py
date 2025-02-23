MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -2

def S(a, b):
    return MATCH_SCORE if a == b else MISMATCH_SCORE

def generateGrid():
    grid = []

    # Initialization step
    for y in range(len(sequence2) + 1): grid.append([GAP_SCORE * y])

    for x in range(1, len(sequence1) + 1): grid[0].append(GAP_SCORE * x)

    # Filling the grid
    for y in range(len(sequence2)):
        for x in range(len(sequence1)):
            grid[y+1].append(max(grid[y][x] + S(sequence1[x],sequence2[y]), grid[y][x+1] + GAP_SCORE, grid[y+1][x] + GAP_SCORE))
    
    return grid

def backtracking(x, y):
    global output1, output2
    if x >= 0 and y >= 0:
        diag = grid[y][x] + S(sequence1[x], sequence2[y])
        left = grid[y+1][x] + GAP_SCORE
        up = grid[y][x+1] + GAP_SCORE

        if diag > left and diag > up:
            output1 = sequence1[x] + output1
            output2 = sequence2[y] + output2
            backtracking(x-1, y-1)
        else:
            if diag < left:
                output1 = sequence1[x] + output1
                output2 = '-' + output2
                backtracking(x-1, y)
            elif diag == left:
                if grid[y+1][x] > grid[y][x]:
                    output1 = sequence1[x] + output1
                    output2 = '-' + output2
                    backtracking(x-1, y)
                else:
                    output1 = sequence1[x] + output1
                    output2 = sequence2[y] + output2
                    backtracking(x-1, y-1)
            elif diag < up:
                output1 = '-' + output1
                output2 = sequence2[y] + output2
                backtracking(x, y-1)
            elif diag == up:
                if grid[y][x+1] > grid[y][x]:
                    output1 = '-' + output1
                    output2 = sequence2[y] + output2
                    backtracking(x, y-1)
                else:
                    output1 = sequence1[x] + output1
                    output2 = sequence2[y] + output2
                    backtracking(x-1, y-1)
    elif x < 0 and y >= 0:
        output1 = '-' + output1
        output2 = sequence2[y] + output2
        backtracking(x, y-1)
    elif x >= 0 and y < 0:
        output1 = sequence1[x] + output1
        output2 = '-' + output2
        backtracking(x-1, y)

def printOutput(inputText):
    global sequence1, sequence2, grid, output1, output2
    output1 = output2 = ''
    sequence1, sequence2 = inputText[0], inputText[1]
    grid = generateGrid()
    backtracking(len(sequence1)-1, len(sequence2)-1)
    print(output1, output2, grid[-1][-1])
