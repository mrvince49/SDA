turn_radius

def detectStaticCollision(self, next_waypoint, telemetry, stationary_obstacle):
    #Predict path of plane
    angle_to_waypoint = math.degrees(math.atan((telemetry.longitude-next_waypoint )))
    if telemetry.heading != 

import numpy:
def getPaths(x, y, z):
    
    t = [-4, -3, -2, -1, 0] #we will assume we can constantly get time reliably within one second since telemetry is operating at 1 Hz
    
    #psuedocode
    
    #reads in the moving obstacle and its attributes, which inlude:
    #latitude
    #longitude
    #radius
    #altitude
    latitude = MovingObstacle.latitude
    longitude = MovingObstacle.longitude
    radius = MovingObstacle.sphere_radius
    altitude = MovingObstacle.altitude_msl
    
    
    # determine function for each coordinate (x,y,z)
    xCoefs = np.polynomial.polynomial.polyfit(t, x, 2)
    yCoefs = 

#flight path = velocity*t + currentPosition
#first time through this method will not work because there is not enough data yet
#after that, we can use previous position and current position and total time it took
#the object to move to its current position




#Check obstacles
#Given: p.lat, p.lon, p.alt, p.spd
		o.lat, o.lon, o.alt, o.rad

#funct:	coord2meter, meter2coord, dist(loc1, loc2), spd()

numSavedPoints
xPositions = []
yPositions = []
zPositions = []


vel = 0; o_Loc = (o.lat,o.lon,o.alt);
	while true
		time.wait(1);
		o_Loc_New = (o.lat,o.lon,o.alt);
		vel = coord2meter(o_Loc_New - o_Loc);
	    o_Loc = o_Loc_New;
	    getPaths(xPositions, yPositions, zPositions)

#super helpful way of calculating linear or quadratic fit
import numpy.polynomial.polynomial as poly
coefs = np.polynomial.polynomial.polyfit(x, y, degreeNum (so 2 in our case))
# we can use 1 for linear fit?
# we need at least two data points for linear fit, three points for quadratic fit
#x and y are arays
#coefs is an array with the coefficients ordered like so:
# [A,B,C] = A + BX + CX^2

#20 m/s TOP SPEED  should low ball at 15 m/s  
#I'm giving it all she's got!! *Scottish accent*




























      ##############################################
                   #
                   #
                   #
                   #
                   #
                   #
                   #
                   #      #        #     #   #####    
                   #      #        #     # #      #
                   #      #        #     ##       #
                   #      #        #     #        #
                   #      #        #     #        #
                   #      #        #     #        #
       #           #      #        #     #        #
       #           #      #        #     #        #
        #         #        #      ##     #        #
          # # # #           ###### #     #        #
