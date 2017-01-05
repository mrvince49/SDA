"""
Convert latitude and longitude to cartesian coordinates
Uses spherical coordinates to find points on the surface of the earth
Values are all in meters. The 'x axis' runs through the center of the earth to 0 and 180 degrees latitude. The 'y axis' runs through the center of the earth to 90 and 270 degrees latitude. The 'z axis' runs up and down the Earth.
"""

import math
def convert_coord(latitude, longitude):
    R = 6371000     #radius of the earth
    la = math.radians(latitude)
    lo = math.radians(longitude)
    x = R * math.cos(lo) * math.cos(la)
    y = R * math.cos(lo) * math.sin(la)
    z = R * math.sin(lo)
    return ("(%d, %d, %d)" %(x, y, z))
