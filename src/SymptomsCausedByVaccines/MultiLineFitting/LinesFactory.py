from skspatial.objects import Line
from SymptomsCausedByVaccines.MultiLineFitting.MultiLineFitter import MultiLineFitter


class LinesFactory:

    @staticmethod
    def createLines(points):
        lines = [Line.from_points(pointA, pointB) for (pointA, pointB) in LinesFactory._getPairs(points)]
        return LinesFactory._getUniqueLines(lines)

    @staticmethod
    def _getPairs(points):
        return ((points[i], points[j]) for (i, j) in MultiLineFitter._getPairs(len(points)))

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
