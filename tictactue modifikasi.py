import tkinter as tk
from tkinter import messagebox
import random
import winsound

root = tk.Tk()
root.title("Tic Tac Toe Pro")
root.geometry("360x480")
root.resizable(False, False)

# ===================== GLOBAL VARIABLES =====================
current_player = "X"  # Player = X, Bot = O
board = ["_"] * 9
buttons = [[None for _ in range(3)] for _ in range(3)]
timer_value = 5
timer_running = False

# ===================== SOUND EFFECT =========================
def click_sound():
    winsound.Beep(1800, 60)

def win_sound():
    winsound.Beep(900, 200)
    winsound.Beep(1200, 200)

# ===================== TIMER ===============================
def start_timer():
    global timer_value, timer_running
    timer_value = 6
    timer_running = True
    update_timer()

def update_timer():
    global timer_value, timer_running

    if not timer_running:
        return

    timer_label.config(text=f"Time: {timer_value}s")

    if timer_value == 0:
        messagebox.showinfo("Waktu Habis", "Waktu habis! Giliran otomatis berpindah.")
        switch_turn()
        return

    timer_value -= 1
    root.after(1000, update_timer)

# ===================== HIGHLIGHT GILIRAN ====================
def update_turn_highlight():
    if current_player == "X":
        label_x.config(fg="#00ff99")
        label_o.config(fg="#cccccc")
    else:
        label_x.config(fg="#cccccc")
        label_o.config(fg="#00ff99")

# ===================== BOT MOVE ============================
def bot_move():
    global current_player

    empty_cells = [i for i in range(9) if board[i] == "_"]
    if not empty_cells:
        return

    choice = random.choice(empty_cells)
    r = choice // 3
    c = choice % 3

    board[choice] = "O"
    buttons[r][c].config(text="O", fg="#ff3b3b")

    click_sound()

    winner = check_winner()
    if winner:
        win_sound()
        messagebox.showinfo("Pemenang", f"Pemain {winner} Menang!")
        reset_board()
        return

    if check_draw():
        messagebox.showinfo("Seri", "Pertandingan Seri!")
        reset_board()
        return

    current_player = "X"
    update_turn_highlight()
    start_timer()

# ===================== CEK PEMENANG =========================
def check_winner():
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] != "_":
            highlight_win(a, b, c)
            return board[a]
    return None

def highlight_win(a, b, c):
    for idx in [a, b, c]:
        r = idx // 3
        c = idx % 3
        buttons[r][c].config(bg="#00cc66")

# ===================== CEK SERI ============================
def check_draw():
    return "_" not in board

# ===================== RESET BOARD =========================
def reset_board():
    global board, current_player, timer_running
    board = ["_"] * 9
    current_player = "X"
    timer_running = False

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="#ffffff")

    update_turn_highlight()

# ===================== SWITCH TURN =========================
def switch_turn():
    global current_player
    current_player = "O"
    update_turn_highlight()
    bot_move()

# ===================== PLAYER CLICK =========================
def on_click(i, j):
    global current_player, timer_running

    idx = i * 3 + j

    if board[idx] != "_" or current_player != "X":
        return

    board[idx] = "X"
    buttons[i][j].config(text="X", fg="#007bff")

    click_sound()

    winner = check_winner()
    if winner:
        win_sound()
        messagebox.showinfo("Pemenang", f"Pemain {winner} Menang!")
        reset_board()
        return

    if check_draw():
        messagebox.showinfo("Seri", "Pertandingan Seri!")
        reset_board()
        return

    current_player = "O"
    timer_running = False
    update_turn_highlight()

    root.after(500, bot_move)

# ===================== UI ================================

title = tk.Label(root, text="Tic Tac Toe PRO", font=("Arial", 20, "bold"))
title.pack(pady=10)

# Turn Indicator
turn_frame = tk.Frame(root)
turn_frame.pack()

label_x = tk.Label(turn_frame, text="Player X", font=("Arial", 14))
label_o = tk.Label(turn_frame, text="Bot O", font=("Arial", 14))
label_x.grid(row=0, column=0, padx=20)
label_o.grid(row=0, column=1, padx=20)

timer_label = tk.Label(root, text="Time: 5s", font=("Arial", 14))
timer_label.pack(pady=5)

update_turn_highlight()

# Board 3x3
frame = tk.Frame(root)
frame.pack(pady=20)

def on_hover_enter(btn):
    btn.config(bg="#e6f7ff")

def on_hover_leave(btn):
    btn.config(bg="#ffffff")

for i in range(3):
    for j in range(3):
        btn = tk.Button(
            frame,
            text="", font=("Arial", 26),
            width=4, height=1,
            bg="#ffffff",
            command=lambda i=i, j=j: on_click(i, j)
        )
        btn.grid(row=i, column=j, padx=6, pady=6)
        btn.bind("<Enter>", lambda e, b=btn: on_hover_enter(b))
        btn.bind("<Leave>", lambda e, b=btn: on_hover_leave(b))
        buttons[i][j] = btn

start_timer()
root.mainloop()