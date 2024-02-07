import unittest
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_walls(self):
        num_cols = 12
        num_rows = 10
        mb = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(mb._cells[0][0].has_top_wall, False)
        self.assertEqual(mb._cells[num_cols - 1][num_rows - 1].has_right_wall, False)


if __name__ == "__main__":
    unittest.main()
