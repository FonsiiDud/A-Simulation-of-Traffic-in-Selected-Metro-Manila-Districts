from trafficSimulator import *

# Create simulation
sim = Simulation()

# Road Network Points
a = (0,0)
b = (101.7, -59.4)
c = (71.1, 14.25)
d = (-11.85, 30.5)
e = (-15, 75)
f = (45, 75)
g = (-71.4, -35.7)
h = (-12.75, -67.35)
i = (-70.8, 14.85)
j = (-45.3, -22.5)

# Road Network
road_1 = g, a
road_2 = a, c
road_3 = a, b
road_4 = h, j
road_5 = i, j
road_6 = a, d
road_7 = d, e
road_8 = b, c
road_9 = c, f
road_10 = g, h
road_11 = h, b
road_12 = f, e
road_13 = e, i
road_14 = i, g

# Append to road list
road_list = [road_1, road_2, road_3, road_4, road_5, road_6, road_7, road_8, road_9, road_10, road_11, road_12, road_13, road_14]

# Create road network
sim.create_roads(road_list)



# Start simulation
win = Window(sim)
win.zoom = 8
win.run(steps_per_update=5)
