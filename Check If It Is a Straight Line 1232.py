def checkStraightLine(coordinates: list):
    if len(coordinates) == 2:
        return True
    else:
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]

        for i in coordinates:
            if ((i[0] - x1) * (y2 - y1) - (x2 - x1) * (i[1] - y1)) != 0:
                return False
        else:
            return True


coordinates = [[0,0],[0,1],[0,-1]]
print(checkStraightLine(coordinates))

