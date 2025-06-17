# main.py

import tkinter as tk
from generator import generate
from utils import print_grid
import time

N = 9
CELL_SIZE = 50
DELAY_MS = 20

class SudokuGUI:
    def __init__(self, master, grid):
        self.master = master
        self.grid = grid
        self.running = False
        self.paused = False

        self.canvas = tk.Canvas(master, width=N*CELL_SIZE, height=N*CELL_SIZE)
        self.canvas.pack()

        self.generate_btn = tk.Button(master, text="Generate", command=self.on_generate)
        self.generate_btn.pack(side=tk.LEFT)

        self.pause_btn = tk.Button(master, text="Pause", command=self.on_pause)
        self.pause_btn.pack(side=tk.LEFT)

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(N):
            for j in range(N):
                x1 = j * CELL_SIZE
                y1 = i * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                val = self.grid[i][j]
                fill = "white" if val == 0 else "#e0f7fa"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="black", tags=f"cell_{i}_{j}")
                if val != 0:
                    self.canvas.create_text(x1 + CELL_SIZE/2, y1 + CELL_SIZE/2, text=str(val), font=("Arial", 16))

    def step_by_step_draw(self):
        self.draw_grid()
        self.master.update_idletasks()
        time.sleep(DELAY_MS / 1000)

    def on_generate(self):
        self.grid = [[0 for _ in range(N)] for _ in range(N)]
        self.running = True
        self.paused = False

        def step(r, c, val):
            self.grid[r][c] = val
            self.step_by_step_draw()

        generate(self.grid, on_step=step)
        self.draw_grid()

    def on_pause(self):
        self.paused = not self.paused

if __name__ == "__main__":
    grid = [[0 for _ in range(N)] for _ in range(N)]

    root = tk.Tk()
    root.title("Sudoku Generator")
    app = SudokuGUI(root, grid)
    root.mainloop()
