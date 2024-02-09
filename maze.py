from cell import Cell
from graphics import Line, Point
import random
import time


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed

        self._create_cells()
        self._break_entrance_exit()

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

    def _break_entrance_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        # Need to account for a cell being at the edge within the maze. That option must be eliminated
        # Need to think through how to populate the not_visisted array
        self._cells[i][j] = True
        while True:
            adj_cells = [
                self._cells[i - 1][j],
                self._cells[i + 1][j],
                self._cells[1][j - 1],
                self._cells[1][j + 1],
            ]
            pos_dir = []
            for cell in adj_cells:
                if not cell._visited and cell in self._cells:
                    pos_dir.append(cell)

            if len(pos_dir) == 0:
                self._draw_cell(i, j)
                return
            else:
                rand_adj_cell = random.randrange(0, len(pos_dir) - 1)
                top_line = Line(
                    Point(self._cells[i][j]._x1, self._cells[i][j]._y1),
                    Point(self._cells[i][j]._x2, self._cells[i][j]._y1),
                )
                left_line = Line(
                    Point(self._cells[i][j]._x1, self._cells[i][j]._y1),
                    Point(self._cells[i][j]._x1, self._cells[i][j]._y2),
                )
                right_line = Line(
                    Point(self._cells[i][j]._x2, self._cells[i][j]._y1),
                    Point(self._cells[i][j]._x2, self._cells[i][j]._y2),
                )
                bottom_line = Line(
                    Point(self._cells[i][j]._x1, self._cells[i][j]._y2),
                    Point(self._cells[i][j]._x2, self._cells[i][j]._y2),
                )

                adj_top_line = Line(
                    Point(self.rand_adj_cell._x1, self.rand_adj_cell._y1),
                    Point(self.rand_adj_cell._x2, self.rand_adj_cell._y1),
                )
                adj_left_line = Line(
                    Point(self.rand_adj_cell._x1, self.rand_adj_cell._y1),
                    Point(self.rand_adj_cell._x1, self.rand_adj_cell._y2),
                )
                adj_right_line = Line(
                    Point(self.rand_adj_cell._x2, self.rand_adj_cell._y1),
                    Point(self.rand_adj_cell._x2, self.rand_adj_cell._y2),
                )
                adj_bottom_line = Line(
                    Point(self.rand_adj_cell._x1, self.rand_adj_cell._y2),
                    Point(self.rand_adj_cell._x2, self.rand_adj_cell._y2),
                )

                if top_line == adj_bottom_line:
                    self._cells[i][j].has_top_wall = False
                    rand_adj_cell.has_bottom_wall = False
                    self._break_walls_r(i - 1, j)
                if left_line == adj_right_line:
                    self._cells[i][j].has_left_wall = False
                    rand_adj_cell.has_right_wall = False
                    self._break_walls_r(i, j + 1)
                if right_line == adj_left_line:
                    self._cells[i][j].has_right_wall = False
                    rand_adj_cell.has_left_wall = False
                    self._break_walls_r(i, j - 1)
                if bottom_line == adj_top_line:
                    self._cells[i][j].has_bottom_wall = False
                    rand_adj_cell.has_top_wall = False
                    self._break_walls_r(i + 1, j)

                # Compare current cell with rand_adj_cell's x and y values to determine which walls need to be knocked down for each cell. Since each cell has their own wall, each cell's wall need to be flagged as false.
