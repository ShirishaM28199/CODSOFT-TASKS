# Task 2 for CodSoft: Tic-Tac-Toe with Minimax AI
import math

def display_board(b):
    for row in [b[i:i+3] for i in range(0, 9, 3)]:
        print("| " + " | ".join(row) + " |")

def check_win(b, p):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    return any(all(b[i] == p for i in s) for s in wins)

def minimax(b, depth, is_max):
    if check_win(b, "O"): return 1
    if check_win(b, "X"): return -1
    if " " not in b: return 0

    if is_max:
        best = -float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, depth + 1, False))
                b[i] = " "
        return best
    else:
        best = float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, depth + 1, True))
                b[i] = " "
        return best

def play():
    board = [" "] * 9
    print("--- Tic-Tac-Toe: You (X) vs Smart AI (O) ---")
    display_board(board)

    while " " in board:
        # User turn
        try:
            move = int(input("Pick a spot (0-8): "))
            if board[move] != " ": continue
            board[move] = "X"
        except: continue

        # AI turn using Minimax
        if " " in board:
            best_score = -float('inf')
            best_move = 0
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(board, 0, False)
                    board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
            board[best_move] = "O"
            print(f"AI picked: {best_move}")
        
        display_board(board)
        if check_win(board, "X"): print("Wait, you won?!"); break
        if check_win(board, "O"): print("AI wins again!"); break
    else: print("It's a tie!")

if __name__ == "__main__":
    play()