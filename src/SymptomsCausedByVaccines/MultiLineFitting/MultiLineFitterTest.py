import unittest
import numpy as np
from skspatial.objects import Line
from SymptomsCausedByVaccines.MultiLineFitting.MultiLineFitter import MultiLineFitter


class MultiLineFitterTest(unittest.TestCase):

    def test_createPreferenceMatrix(self):
        # Given
        points = [(1, 3), (10, 20)]
        lines = [Line.from_points([0, 0], [100, 0])]
        consensusThreshold = 4.0

        # When
        preferenceMatrix = MultiLineFitter._createPreferenceMatrix(points, lines, consensusThreshold)

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
        preferenceMatrix = MultiLineFitter._createPreferenceMatrix(points, lines, consensusThreshold)

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
        clusters, _ = MultiLineFitter._createClusters(preferenceMatrix)

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
        clusters, preferenceMatrix4Clusters = MultiLineFitter._createClusters(preferenceMatrix)

        # Then
        np.testing.assert_array_equal(
            clusters,
            np.array(
                [
                    [2, 1, 0],
                    [4, 3]
                ]))
        np.testing.assert_array_equal(
            preferenceMatrix4Clusters,
            np.array(
                [
                    [1, 0],
                    [0, 1]
                ]))

    def test_getLineIndexes(self):
        # Given
        preferenceMatrix = np.array(
                [
                    [0, 0, 1],
                    [0, 1, 1]
                ])

        # When
        lineIndexes = MultiLineFitter._getLineIndexes(preferenceMatrix)

        # Then
        np.testing.assert_array_equal(lineIndexes, [2, 1])

    def test_fitLines(self):
        # Given
        points = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 2), (3, 3)]
        line1 = Line.from_points([0, 0], [1, 0])
        line2 = Line.from_points([0, 0], [1, 1])
        line3 = Line.from_points([0, 0], [0, 1])

        # When
        clusters, fittedLines = MultiLineFitter.fitLines(points, lines = [line1, line2, line3], consensusThreshold = 0.001)

        # Then
        np.testing.assert_array_equal(
            fittedLines,
            [
                line1,
                line2
            ])
        np.testing.assert_array_equal(
            clusters,
            [
                [(1, 0), (2, 0), (3, 0)],
                [(1, 1), (2, 2), (3, 3)]
            ])

    def test_fitPointsByLines(self):
        # Given
        points = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 2), (3, 3)]

        # When
        clusters, lines = MultiLineFitter.fitPointsByLines(points, consensusThreshold = 0.001)

        # Then
        self.assertEqual(len(lines), 2)
        self.assertTrue(lines[0].is_close(Line.from_points([0, 0], [1, 0])))
        self.assertTrue(lines[1].is_close(Line.from_points([0, 0], [1, 1])))
        np.testing.assert_array_equal(
            clusters,
            [
                [(1, 0), (2, 0), (3, 0)],
                [(1, 1), (2, 2), (3, 3)]
            ])
