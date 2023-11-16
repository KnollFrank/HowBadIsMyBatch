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
            bestClusterIndexCombo = None
            keepClustering = False
            numClusters = preferenceMatrix.shape[0]
            for clusterIndexA in range(numClusters):
                preferenceSetA = preferenceMatrix[clusterIndexA]
                for clusterIndexB in range(clusterIndexA):
                    preferenceSetB = preferenceMatrix[clusterIndexB]
                    distance = ClustersFactory._intersectionOverUnion(preferenceSetA, preferenceSetB);
                    if distance > maxDistance:
                        keepClustering = True
                        maxDistance = distance
                        bestClusterIndexCombo = (clusterIndexA, clusterIndexB)

            if keepClustering:
                (clusterIndexA, clusterIndexB) = bestClusterIndexCombo
                clusters[clusterIndexA] += clusters[clusterIndexB]
                clusters.pop(clusterIndexB)
                preferenceMatrix[clusterIndexA] = np.logical_and(preferenceMatrix[clusterIndexA], preferenceMatrix[clusterIndexB])
                preferenceMatrix = np.delete(preferenceMatrix, clusterIndexB, axis = 0)

        return clusters

    @staticmethod
    def _intersectionOverUnion(set_a, set_b):
        intersection = np.count_nonzero(np.logical_and(set_a, set_b))
        union = np.count_nonzero(np.logical_or(set_a, set_b))
        return 1. * intersection / union
