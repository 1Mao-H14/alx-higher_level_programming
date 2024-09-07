#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_not_a_number_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_too_small_and_exit():
    print("N must be at least 4")
    sys.exit(1)

def is_safe(board, row, col, n):
    # Check this column on the left side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, row, n, solutions):
    if row >= n:
        # Collect the solution in the format [[row1, col1], [row2, col2], ...]
        solution = [[r, c.index(1)] for r, c in enumerate(board)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print_not_a_number_and_exit()

    if n < 4:
        print_too_small_and_exit()

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
