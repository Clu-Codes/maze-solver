from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Runner")
        self.__canvas = Canvas(self.__root, width=self.__width, height=self.__height)
        self.__canvas.pack(fill=BOTH)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)


class Cell:
    def __init__(
        self,
        x1,
        y1,
        x2,
        y2,
        window,
        left_wall=True,
        right_wall=True,
        bottom_wall=True,
        top_wall=True,
    ):
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            left_line = Line(top_left, bottom_left)
            self._win.draw_line(left_line, fill_color="white")

        if self.has_bottom_wall:
            bottom_line = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_line, fill_color="white")

        if self.has_right_wall:
            right_line = Line(top_right, bottom_right)
            self._win.draw_line(right_line, fill_color="white")

        if self.has_top_wall:
            top_line = Line(top_left, top_right)
            self._win.draw_line(top_line, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        line_color = None
        if undo == False:
            line_color = "red"
        else:
            line_color = "grey"

        center = Point(
            self._x1 + (self._x2 - self._x1) / 2, (self._y1 + (self._y2 - self._y1) / 2)
        )
        to_cell_center = Point(
            to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2,
            to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2,
        )
        line = Line(center, to_cell_center)

        self._win.draw_line(line, line_color)


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

    def _create_cells(self):
        self._cells = []
        cell_val = Cell(
            self._x1,
            self._y1,
            self._x1 * self._cell_size_x,
            self._y1 * self._cell_size_y,
            self._win,
        )
        for column in range(self._num_cols):
            self._cells.append([cell_val])
            for row in range(self._num_rows):
                self._cells[column].append(cell_val)

        for list in self._cells:
            for cell in list:
                cell._draw_cell(list, cell)

    def _draw_cell(self, i, j):
        self.draw()
