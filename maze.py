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
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

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
        time.sleep(0.025)

    def _break_entrance_exit(self, entrance_cell, exit_cell):
        if self._win is None:
            return

        if self._cells[entrance_cell].has_top_wall:
            repaint_entry = Line(
                Point(self._cells[entrance_cell]._x1, self._cells[entrance_cell]._y1),
                (self._cells[entrance_cell]._x2, self._cells[entrance_cell]._y1),
            )
            self._cells[entrance_cell].self._win.draw_line(repaint_entry)
            self._cells[entrance_cell].has_top_wall = False

        if self._cells[entrance_cell].has_right_wall:
            repaint_exit = Line(
                Point(self._cells[entrance_cell]._x2, self._cells[entrance_cell]._y1),
                (self._cells[entrance_cell]._x2, self._cells[entrance_cell]._y2),
            )
            self._cells[entrance_cell].self_win.draw_line(repaint_exit)
            self._cells[exit_cell].has_right_wall = False
