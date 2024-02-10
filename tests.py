import unittest
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(
            0, 0, num_rows, num_cols, 10, 10, win=None, seed=None, break_walls=False
        )
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_walls(self):
        num_cols = 12
        num_rows = 10
        mb = Maze(0, 0, num_rows, num_cols, 10, 10, win=None, seed=None)
        self.assertEqual(mb._cells[0][0].has_top_wall, False)
        self.assertEqual(mb._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_break_walls_r(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=None, seed=0)

        for i in range(num_cols):
            for j in range(num_rows):
                cell = m1._cells[i][j]
                missing_walls = {
                    direction: wall
                    for (direction, wall) in [
                        ("top", cell.has_top_wall),
                        ("bottom", cell.has_bottom_wall),
                        ("left", cell.has_left_wall),
                        ("right", cell.has_right_wall),
                    ]
                    if not wall
                }

                key_list = list(missing_walls.keys())

                if cell._visited:
                    self.assertTrue(
                        not cell.has_top_wall
                        or not cell.has_bottom_wall
                        or not cell.has_left_wall
                        or not cell.has_right_wall
                    )
                    if key_list[0] == "left":
                        self.assertTrue(
                            not cell.has_left_wall,
                            not m1._cells[i - 1][j].has_right_wall,
                        )
                    if key_list[0] == "right":
                        self.assertTrue(
                            not cell.has_right_wall,
                            not m1._cells[i + 1][j].has_left_wall,
                        )
                    if key_list[0] == "up":
                        self.assertTrue(
                            not cell.has_top_wall,
                            not m1._cells[i][j - 1].has_bottom_wall,
                        )
                    if key_list[0] == "down":
                        self.assertTrue(
                            not cell.has_bottom_wall,
                            not m1._cells[i][j + 1].has_top_wall,
                        )


if __name__ == "__main__":
    unittest.main()
