import unittest

from Bowling import Bowling


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bowling_class = Bowling()

    @unittest.skip
    def test_environment(self):
        self.assertEqual(True, False)

    def _roll_number_balls(self, number_balls):
        self.bowling_class.roll_balls(number_balls)

    def test_bowling_initialization(self):
        self.assertEqual(10, self.bowling_class.get_number_frames_left())
        self.assertEqual(0, self.bowling_class.get_current_score())

    def test_bowl_one_frame_zeros(self):
        self._roll_number_balls(0)
        self._roll_number_balls(0)
        self.assertEqual(9, self.bowling_class.get_number_frames_left())

    def test_bowl_one_frame_strike(self):
        self._roll_number_balls(10)
        self.assertEqual(9, self.bowling_class.get_number_frames_left())

    def test_score_one(self):
        self._roll_number_balls(1)
        self.assertEqual(1, self.bowling_class.get_current_score())

    @unittest.skip
    def test_score_twenty_two(self):
        self._roll_number_balls(10)
        self._roll_number_balls(0)
        self._roll_number_balls(1)
        self._roll_number_balls(2)
        self._roll_number_balls(3)
        self.assertEqual(22, self.bowling_class.get_current_score())


if __name__ == '__main__':
    unittest.main()
