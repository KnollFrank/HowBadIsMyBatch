import numpy as np
from SymptomsCausedByVaccines.MultiLineFitting.LinesFactory import LinesFactory
from SymptomsCausedByVaccines.MultiLineFitting.Utils import generatePairs
from SymptomsCausedByVaccines.MultiLineFitting.CharacteristicFunctions import CharacteristicFunctions

# implementation of "Robust Multiple Structures Estimation with J-linkage" adapted from https://github.com/fkluger/vp-linkage
class MultiLineFitter:
    
    @staticmethod
    def fitPointsByLines(points, consensusThreshold, maxNumLines = None):
        return MultiLineFitter.fitLines(
            points,
            LinesFactory.createLines(points, maxNumLines),
            consensusThreshold)

    @staticmethod
    def fitPointsByAscendingLines(points, consensusThreshold, maxNumLines = None):
        return MultiLineFitter.fitLines(
            points,
            LinesFactory.createAscendingLines(points, maxNumLines),
            consensusThreshold)

    @staticmethod
    def fitLines(points, lines, consensusThreshold):
        preferenceMatrix = MultiLineFitter._createPreferenceMatrix(points, lines, consensusThreshold)
        _, preferenceMatrix4Clusters = MultiLineFitter._createClusters(preferenceMatrix)
        fittedLines = MultiLineFitter._getLines(lines, preferenceMatrix4Clusters)
        return (
            MultiLineFitter._getFittedPointsList(points, fittedLines, consensusThreshold),
            fittedLines)

    @staticmethod
    def _getFittedPointsList(points, lines, consensusThreshold):
        return MultiLineFitter._getPointsList(
            points,
            MultiLineFitter._createPreferenceMatrix(points, lines, consensusThreshold))

    @staticmethod
    def _getPointsList(points, preferenceMatrix):
        characteristicFunctionsOfConsensusSets = np.transpose(preferenceMatrix)
        return [CharacteristicFunctions.apply(characteristicFunctionOfConsensusSet, points) for characteristicFunctionOfConsensusSet in characteristicFunctionsOfConsensusSets]

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
            maxSimilarity = 0
            bestClusterIndexCombination = None
            keepClustering = False
            numClusters = preferenceMatrix.shape[0]
            for (clusterIndexA, clusterIndexB) in generatePairs(numClusters):
                preferenceSetA = preferenceMatrix[clusterIndexA]
                preferenceSetB = preferenceMatrix[clusterIndexB]
                similarity = MultiLineFitter._intersectionOverUnion(preferenceSetA, preferenceSetB);
                if similarity > maxSimilarity:
                    keepClustering = True
                    maxSimilarity = similarity
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
        return 1. * intersection / union if intersection > 0.0 else 0

    @staticmethod
    def _getLines(lines, preferenceMatrix):
        return np.array(lines)[MultiLineFitter._getLineIndexes(preferenceMatrix)]

    @staticmethod
    def _getLineIndexes(preferenceMatrix):
        lineIndexes = (MultiLineFitter._index(lines, 1) for lines in preferenceMatrix)
        return [lineIndex for lineIndex in lineIndexes if lineIndex is not None]

    @staticmethod
    def _index(xs, x):
        try:
            return list(xs).index(x)
        except ValueError:
            return None

    @staticmethod
    def _getClusterPoints(points, clusters):
        sortedClusters = [sorted(cluster) for cluster in clusters]
        return [list(np.array(points)[cluster]) for cluster in sortedClusters]