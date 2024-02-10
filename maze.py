from cell import Cell
from graphics import Line, Point
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
        break_walls=True,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_exit()
        if break_walls:
            self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _break_entrance_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            pos_dir = []
            if i > 0 and not self._cells[i - 1][j]._visited:
                pos_dir.append((self._cells[i - 1][j], "left"))
            if i < self._num_cols - 1 and not self._cells[i + 1][j]._visited:
                pos_dir.append((self._cells[i + 1][j], "right"))
            if j > 0 and not self._cells[i][j - 1]._visited:
                pos_dir.append((self._cells[i][j - 1], "up"))
            if j < self._num_rows - 1 and not self._cells[i][j + 1]._visited:
                pos_dir.append((self._cells[i][j + 1], "down"))

            if len(pos_dir) == 0:
                self._draw_cell(i, j)
                return
            else:
                rand_adj_cell, direction = random.choice(pos_dir)

                if direction == "left":
                    self._cells[i][j].has_left_wall = False
                    rand_adj_cell.has_right_wall = False
                    self._break_walls_r(i - 1, j)
                if direction == "down":
                    self._cells[i][j].has_bottom_wall = False
                    rand_adj_cell.has_top_wall = False
                    self._break_walls_r(i, j + 1)
                if direction == "up":
                    self._cells[i][j].has_top_wall = False
                    rand_adj_cell.has_bottom_wall = False
                    self._break_walls_r(i, j - 1)
                if direction == "right":
                    self._cells[i][j].has_right_wall = False
                    rand_adj_cell.has_left_wall = False
                    self._break_walls_r(i + 1, j)
