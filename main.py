from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    # point1 = Point(50, 100)
    # point2 = Point(30, 60)
    # line = Line(point1, point2)

    cell1 = Cell(
        10,
        15,
        20,
        25,
        win,
        left_wall=True,
        right_wall=False,
        top_wall=True,
        bottom_wall=True,
    )
    cell2 = Cell(
        20,
        40,
        60,
        80,
        win,
        left_wall=True,
        right_wall=True,
        top_wall=False,
        bottom_wall=True,
    )
    cell3 = Cell(
        100,
        125,
        150,
        175,
        win,
        left_wall=True,
        right_wall=True,
        top_wall=True,
        bottom_wall=False,
    )
    cell4 = Cell(
        300,
        320,
        340,
        360,
        win,
        left_wall=False,
        right_wall=True,
        top_wall=True,
        bottom_wall=True,
    )

    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()

    # win.draw_line(line, fill_color="blue")
    win.wait_for_close()


if __name__ == "__main__":
    main()
