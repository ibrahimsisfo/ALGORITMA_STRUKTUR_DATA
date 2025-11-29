import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")
root.resizable(False, False)

current_player = "X"
board = [""] * 9
buttons = [[None for _ in range(3)] for _ in range(3)]

# ===================== RESET BOARD =====================
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# ===================== CEK PEMENANG =====================
def check_winner():
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    return None

# ===================== CEK SERI =====================
def check_draw():
    return all(cell != "" for cell in board)

# ===================== PLAYER CLICK =====================
def on_click(i, j):
    global current_player
    idx = i * 3 + j

    if board[idx] != "":
        return

    board[idx] = current_player
    buttons[i][j].config(text=current_player)

    winner = check_winner()
    if winner:
        messagebox.showinfo("Winner", f"Player {winner} wins!")
        reset_board()
        return

    if check_draw():
        messagebox.showinfo("Draw", "It's a draw!")
        reset_board()
        return

    current_player = "O" if current_player == "X" else "X"

# ===================== UI =====================

title = tk.Label(root, text="Tic Tac Toe", font=("Arial", 20, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(
            frame, text="", font=("Arial", 24),
            width=4, height=1,
            command=lambda i=i, j=j: on_click(i, j)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

root.mainloop()