import numpy as np
from startSDA import getObstacles

#initialize variables
numSavedPoints
movingObstaclesData = [] #array of size numSavedPoints of moving
                         #moving is an array of movingObstacles at a certain point in time
stationary, moving = getObstacles()

movingObstaclesData.append(moving) #add initial obstacle data

while true: #modify to update along with telemetry
    stationary, moving = getObstacles()
    #add new data to the array, get rid of old data
    if (movingObstaclesData.len() >= numSavedPoints):
        movingObstaclesData.append(moving)
        del movingObstaclesData[0]
    else:
        movingObstaclesData.append(moving)
    paths = calculate(movingObstaclesData)

    #For testin
    for movingObstaclePath in paths:
        print "x = " + movingObstaclePath[0][0] + "t + " + movingObstaclePath[0][1]
        print "y = " + movingObstaclePath[1][0] + "t + " + movingObstaclePath[1][1]
        print "z = " + movingObstaclePath[2][0] + "t + " + movingObstaclePath[2][1]


def calculate(self, movingObstacleData):
    paths = [] #array of movingObstacles; each contains x,y,z linear regression; each contains coeffs for y = a + bx
    time = range((numSavedPoints - 1) * -1, 0)
    xPositions = [] #arrays of movingObstacles; each contains component position for all past times
    yPositions = [] 
    zPositions = []

    #Fill in x,y,z position arrays
    for index in range(0, numSavedPoints):
        moving = movingObstacleData[index]
        for index2 in range(0, moving.len()):
            movingObstacle = moving[index2]
            xPositions[index2].append(movingObstacle.longitude) #change to coordinate plane?
            yPositions[index2].append(movingObstacle.latitude)
            zPositions[index2].append(movingObstacle.altitude)
            if (xPositions.len() > numSavedPoints):
                del xPositions[0]
            if (yPositions.len() > numSavedPoints):
                del yPositions[0]
            if (zPositions.len() > numSavedPoints):
                del zPositions[0]

    #Calculate paths, enter into array
    for index3 in range(0, movingOsbtacleData[0].len()):
        xCoefs = np.polynomial.polynomial.polyfit(time, xPositions[index3])
        yCoefs = np.polynomial.polynomial.polyfit(time, yPositions[index3])
        zCoefs = np.polynomial.polynomial.polyfit(time, zPositions[index3])
        paths[index3].append([xCoefs, yCoefs, zCoefs])

    return paths


