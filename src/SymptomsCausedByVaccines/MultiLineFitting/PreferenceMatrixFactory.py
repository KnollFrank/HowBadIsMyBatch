import numpy as np
from skspatial.objects import Line

class PreferenceMatrixFactory:

    @staticmethod
    def createPreferenceMatrix(points, lines, consensusThreshold):
        preferenceMatrix = np.zeros([len(points), len(lines)], dtype = int)
        for pointIndex, point in enumerate(points):
            for lineIndex, line in enumerate(lines):
                preferenceMatrix[pointIndex, lineIndex] = 1 if line.distance_point(point) <= consensusThreshold else 0

        return preferenceMatrix
    
