import random
import copy

def pattern(r, c): return (3 * (r % 3) + r // 3 + c) % 9

def shuffle(s): return random.sample(s, len(s))

def generate_full_board():
    base = 3
    rows = [g * base + r for g in shuffle(range(base)) for r in shuffle(range(base))]
    cols = [g * base + c for g in shuffle(range(base)) for c in shuffle(range(base))]
    nums = shuffle(range(1, 10))
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]
    return board

def remove_cells(board, num_remove=45):
    puzzle = copy.deepcopy(board)
    removed = 0
    while removed < num_remove:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if puzzle[r][c] != 0:
            puzzle[r][c] = 0
            removed += 1
    return puzzle

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += str(board[i][j]) + " " if board[i][j] != 0 else ". "
        print(row_str)

def is_board_full(board):
    return all(board[i][j] != 0 for i in range(9) for j in range(9))

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def play_game():
    full_board = generate_full_board()
    puzzle = remove_cells(full_board, num_remove=random.randint(40, 50))
    solution = copy.deepcopy(puzzle)
    solve_sudoku(solution)

    board = copy.deepcopy(puzzle)

    print("\nWelcome to Sudoku!")
    print("Instructions:")
    print("Enter your move in format: row col number")
    print("Type 'exit' to quit the game.\n")

    while not is_board_full(board):
        print_board(board)

        user_input = input("\nYour move (row col num): ").strip()
        if user_input.lower() == "exit":
            print("Thanks for playing!")
            return

        try:
            r, c, n = map(int, user_input.split())
            r -= 1
            c -= 1

            if not (0 <= r < 9 and 0 <= c < 9 and 1 <= n <= 9):
                print("Invalid input. Use numbers 1-9 for row, column, and number.")
                continue

            if puzzle[r][c] != 0:
                print("That cell is pre-filled. You can't change it.")
                continue

            if solution[r][c] == n:
                if board[r][c] == 0:
                    board[r][c] = n
                    print("Correct!")
                else:
                    print("You already entered that correctly.")
            else:
                print("Wrong number. Please try again.")

        except ValueError:
            print("Invalid format. Please enter 3 numbers separated by spaces.")

    print_board(board)
    print("\n Congratulations! You've completed the puzzle!")

if __name__ == "__main__":
    play_game()
