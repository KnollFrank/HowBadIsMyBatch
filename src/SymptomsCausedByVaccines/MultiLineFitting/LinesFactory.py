from skspatial.objects import Line
from SymptomsCausedByVaccines.MultiLineFitting.Utils import generatePairs


class LinesFactory:

    @staticmethod
    def createLines(points):
        return LinesFactory._getUniqueLines(list(LinesFactory._generateAllLines(points)))

    @staticmethod
    def createAscendingLines(points):
        return LinesFactory._getUniqueLines(list(LinesFactory._generateAllAscendingLines(points)))

    @staticmethod
    def _generateAllAscendingLines(points):
        return (line for line in LinesFactory._generateAllLines(points) if LinesFactory._isAscending(line.direction))

    @staticmethod
    def _generateAllLines(points):
        return (Line.from_points(pointA, pointB) for (pointA, pointB) in LinesFactory._generatePairs(points))

    @staticmethod
    def _isAscending(direction):
        return (direction[0] >= 0 and direction[1] >= 0) or (direction[0] <= 0 and direction[1] <= 0)

    @staticmethod
    def _generatePairs(points):
        return ((points[i], points[j]) for (i, j) in generatePairs(len(points)))

    @staticmethod
    def _getUniqueLines(lines):
        uniqueLines = []
        for i in range(len(lines)):
            line = lines[i]
            if not LinesFactory._isLineCloseToAnyOtherLine(line, lines[i + 1:]):
                uniqueLines.append(line)
        return uniqueLines

    @staticmethod
    def _isLineCloseToAnyOtherLine(line, otherLines):
        for otherLine in otherLines:
            if line.is_close(otherLine):
                return True
        return False
