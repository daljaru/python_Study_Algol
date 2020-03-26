#동전 교환문제
m = [[1,5,3],
    [2,5,7],
    [5,3,5]]

col_check = [False, False, False]

min_sol = 10000;

def backtracking(row, score, min_sol):
    if row == 3:
        if score < min_sol:
            min_sol = score
        return min_sol
    for i in range(0, 3):
        if col_check[i] == False:
            col_check[i] = True
            print(col_check)
            min_sol = backtracking(row+1, score+m[row][i], min_sol)
            col_check[i] = False
            print(col_check)
    return min_sol


print(backtracking(0, 0, min_sol))
