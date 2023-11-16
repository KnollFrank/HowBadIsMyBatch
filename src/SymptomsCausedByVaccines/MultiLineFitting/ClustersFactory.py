import numpy as np
from skspatial.objects import Line

class ClustersFactory:

    @staticmethod
    def createPreferenceMatrix(points, lines, consensusThreshold):
        preferenceMatrix = np.zeros([len(points), len(lines)], dtype = int)
        for pointIndex, point in enumerate(points):
            for lineIndex, line in enumerate(lines):
                preferenceMatrix[pointIndex, lineIndex] = 1 if line.distance_point(point) <= consensusThreshold else 0

        return preferenceMatrix
    
    @staticmethod
    def createClusters(preferenceMatrix):
        keepClustering = True
        numClusters = preferenceMatrix.shape[0]
        clusters = [[i] for i in range(numClusters)]
        while keepClustering:
            maxDistance = 0
            bestCombo = None
            keepClustering = False
            numClusters = preferenceMatrix.shape[0]
            for i in range(numClusters):
                set_a = preferenceMatrix[i]
                for j in range(i):
                    set_b = preferenceMatrix[j]
                    distance = ClustersFactory._intersectionOverUnion(set_a, set_b);
                    if distance > maxDistance:
                        keepClustering = True
                        maxDistance = distance
                        bestCombo = (i, j)

            if keepClustering:
                clusters[bestCombo[0]] += clusters[bestCombo[1]]
                clusters.pop(bestCombo[1])
                preferenceMatrix[bestCombo[0]] = np.logical_and(preferenceMatrix[bestCombo[0]], preferenceMatrix[bestCombo[1]])
                preferenceMatrix = np.delete(preferenceMatrix, bestCombo[1], axis = 0)

        return clusters

    @staticmethod
    def _intersectionOverUnion(set_a, set_b):
        intersection = np.count_nonzero(np.logical_and(set_a, set_b))
        union = np.count_nonzero(np.logical_or(set_a, set_b))
        return 1. * intersection / union
