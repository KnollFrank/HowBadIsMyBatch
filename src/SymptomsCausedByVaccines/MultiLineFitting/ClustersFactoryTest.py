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

    def test_createPreferenceMatrix2(self):
        # Given
        points = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 2), (3, 3)]
        lines = [Line.from_points([0, 0], [1, 0]), Line.from_points([0, 0], [1, 1])]
        consensusThreshold = 0.001

        # When
        preferenceMatrix = ClustersFactory.createPreferenceMatrix(points, lines, consensusThreshold)

        # Then
        np.testing.assert_array_equal(
            preferenceMatrix,
            np.array(
                [
                    [1, 0],
                    [1, 0],
                    [1, 0],
                    [0, 1],
                    [0, 1],
                    [0, 1]
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

    def test_createClusters2(self):
        # Given
        preferenceMatrix = np.array(
                [
                    [1, 1],
                    [1, 0],
                    [1, 0],
                    [0, 1],
                    [0, 1]
                ])

        # When
        _, clusters = ClustersFactory.createClusters(preferenceMatrix)

        # Then
        np.testing.assert_array_equal(
            clusters,
            np.array(
                [
                    [2, 1, 0],
                    [4, 3]
                ]))
