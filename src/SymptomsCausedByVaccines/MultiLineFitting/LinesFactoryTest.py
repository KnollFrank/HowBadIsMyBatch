import unittest
from skspatial.objects import Line
from SymptomsCausedByVaccines.MultiLineFitting.LinesFactory import LinesFactory


class LinesFactoryTest(unittest.TestCase):

    def test_createLines(self):
        # Given
        points = [(1, 0), (2, 0), (3, 0)]

        # When
        lines = LinesFactory.createLines(points)

        # Then
        self.assertEqual(len(lines), 1)
        self.assertTrue(lines[0].is_close(Line(point = [0, 0], direction = [1, 0])))

    def test_createLines2(self):
        # Given
        points = [(0, 0), (1, 0), (0, 1)]

        # When
        lines = LinesFactory.createLines(points)

        # Then
        self.assertEqual(len(lines), 3)
        self.assertTrue(lines[0].is_close(Line(point = [0, 0], direction = [1, 0])))
        self.assertTrue(lines[1].is_close(Line(point = [0, 0], direction = [0, 1])))
        self.assertTrue(lines[2].is_close(Line(point = [0, 1], direction = [1, -1])))

    def test_createAscendingLines(self):
        # Given
        points = [(0, 0), (1, 0), (0, 1)]

        # When
        lines = LinesFactory.createAscendingLines(points)

        # Then
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[0].is_close(Line(point = [0, 0], direction = [1, 0])))
        self.assertTrue(lines[1].is_close(Line(point = [0, 0], direction = [0, 1])))
