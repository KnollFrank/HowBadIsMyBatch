import numpy as np
from skspatial.objects import Line

# implementation of "Robust Multiple Structures Estimation with J-linkage" adapted from https://github.com/fkluger/vp-linkage
class MultiLineFitter:
    
    @staticmethod
    def fitLines(points, lines, consensusThreshold):
        preferenceMatrix = MultiLineFitter._createPreferenceMatrix(points, lines, consensusThreshold)
        _, preferenceMatrix4Clusters = MultiLineFitter._createClusters(preferenceMatrix)
        lineIndexes = MultiLineFitter._getLineIndexes(preferenceMatrix4Clusters)
        return [lines[lineIndex] for lineIndex in lineIndexes]

    @staticmethod
    def _createPreferenceMatrix(points, lines, consensusThreshold):
        preferenceMatrix = np.zeros([len(points), len(lines)], dtype = int)
        for pointIndex, point in enumerate(points):
            for lineIndex, line in enumerate(lines):
                preferenceMatrix[pointIndex, lineIndex] = 1 if line.distance_point(point) <= consensusThreshold else 0
        return preferenceMatrix

    @staticmethod
    def _createClusters(preferenceMatrix):
        keepClustering = True
        numClusters = preferenceMatrix.shape[0]
        clusters = [[i] for i in range(numClusters)]
        while keepClustering:
            maxDistance = 0
            bestClusterIndexCombination = None
            keepClustering = False
            numClusters = preferenceMatrix.shape[0]
            for clusterIndexA in range(numClusters):
                preferenceSetA = preferenceMatrix[clusterIndexA]
                for clusterIndexB in range(clusterIndexA):
                    preferenceSetB = preferenceMatrix[clusterIndexB]
                    distance = MultiLineFitter._intersectionOverUnion(preferenceSetA, preferenceSetB);
                    if distance > maxDistance:
                        keepClustering = True
                        maxDistance = distance
                        bestClusterIndexCombination = (clusterIndexA, clusterIndexB)

            if keepClustering:
                (clusterIndexA, clusterIndexB) = bestClusterIndexCombination
                clusters[clusterIndexA] += clusters[clusterIndexB]
                clusters.pop(clusterIndexB)
                preferenceMatrix[clusterIndexA] = np.logical_and(preferenceMatrix[clusterIndexA], preferenceMatrix[clusterIndexB])
                preferenceMatrix = np.delete(preferenceMatrix, clusterIndexB, axis = 0)

        return clusters, preferenceMatrix

    @staticmethod
    def _intersectionOverUnion(setA, setB):
        intersection = np.count_nonzero(np.logical_and(setA, setB))
        union = np.count_nonzero(np.logical_or(setA, setB))
        return 1. * intersection / union

    @staticmethod
    def _getLineIndexes(preferenceMatrix):
        return [list(lines).index(1) for lines in preferenceMatrix]
