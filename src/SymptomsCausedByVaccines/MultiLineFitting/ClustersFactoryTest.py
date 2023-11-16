import unittest
import numpy as np
from skspatial.objects import Line
from src.SymptomsCausedByVaccines.MultiLineFitting.ClustersFactory import ClustersFactory


class ClustersFactoryTest(unittest.TestCase):

    def test_createPreferenceMatrix(self):
        # Given
        points = [(1, 3), (10, 20)]
        lines = [Line.from_points([0, 0], [100, 0])]
        consensusThreshold = 4.0

        # When
        preferenceMatrix = ClustersFactory.createPreferenceMatrix(points, lines, consensusThreshold)

        # Then
        np.testing.assert_array_equal(
            preferenceMatrix,
            np.array(
                [
                    [1],
                    [0]
                ]))

    def test_createClusters(self):
        # Given
        preferenceMatrix = np.array(
                [
                    [1],
                    [1]
                ])

        # When
        _, clusters = ClustersFactory.createClusters(preferenceMatrix)

        # Then
        np.testing.assert_array_equal(
            clusters,
            np.array(
                [
                    [1, 0]
                ]))
