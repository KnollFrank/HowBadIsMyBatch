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
        keep_clustering = True
        cluster_step = 0

        num_clusters = preferenceMatrix.shape[0]
        clusters = [[i] for i in range(num_clusters)]

        while keep_clustering:
            smallest_distance = 0
            best_combo = None
            keep_clustering = False

            num_clusters = preferenceMatrix.shape[0]

            for i in range(num_clusters):
                for j in range(i):
                    set_a = preferenceMatrix[i]
                    set_b = preferenceMatrix[j]
                    intersection = np.count_nonzero(np.logical_and(set_a, set_b))
                    union = np.count_nonzero(np.logical_or(set_a, set_b))
                    distance = 1.*intersection/np.maximum(union, 1e-8)

                    if distance > smallest_distance:
                        keep_clustering = True
                        smallest_distance = distance
                        best_combo = (i,j)

            if keep_clustering:
                clusters[best_combo[0]] += clusters[best_combo[1]]
                clusters.pop(best_combo[1])
                set_a = preferenceMatrix[best_combo[0]]
                set_b = preferenceMatrix[best_combo[1]]
                merged_set = np.logical_and(set_a, set_b)
                preferenceMatrix[best_combo[0]] = merged_set
                preferenceMatrix = np.delete(preferenceMatrix, best_combo[1], axis=0)
                cluster_step += 1

        print("clustering finished after %d steps" % cluster_step)

        return preferenceMatrix, clusters
