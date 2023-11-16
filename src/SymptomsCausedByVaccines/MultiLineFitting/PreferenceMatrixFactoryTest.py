import unittest
import numpy as np
from numpy.testing import assert_array_equal
from skspatial.objects import Line
from SymptomsCausedByVaccines.MultiLineFitting.PreferenceMatrixFactory import PreferenceMatrixFactory


class PreferenceMatrixFactoryTest(unittest.TestCase):

    def test_createPreferenceMatrix(self):
        # Given
        points = [(1, 3), (10, 20)]
        lines = [Line.from_points([0, 0], [100, 0])]
        consensusThreshold = 4.0

        # When
        preferenceMatrix = PreferenceMatrixFactory.createPreferenceMatrix(points, lines, consensusThreshold)

        # Then
        assert_array_equal(
            preferenceMatrix,
            np.array(
                [
                    [1],
                    [0]
                ]))
