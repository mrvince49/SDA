turn_radius

def detectStaticCollision(self, next_waypoint, telemetry, stationary_obstacle):
    #Predict path of plane
    angle_to_waypoint = math.degrees(math.atan((telemetry.longitude-next_waypoint )))
    if telemetry.heading != 
