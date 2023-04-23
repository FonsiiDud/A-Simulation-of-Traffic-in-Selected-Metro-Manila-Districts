from trafficSimulator import *

# Create simulation
sim = Simulation()

# Road Network Points
a = (0,0)
b = (-78.6, 0)
c = (100, 0)
d = (0, -60)
e = (0, 50)
f = (5.7, -92)
g = (27, -114.4)
h = (100.4, -68.0)
i = (-50, -150)
j = (99.7, 79.4)
k = (50, 150)
l = (-47.1, 106.4)
m = (-116.8,  74.9)

# Road Network
road_1 = m,b
road_2 = b,i
road_3 = i,g
road_4 = g,h
road_5 = h,c
road_6 = c,j
road_7 = j,k
road_8 = k,l
road_9 = l,m
road_10 = b,a
road_11 = a,c
road_12 = g,f
road_13 = f,d
road_14 = d,a
road_15 = a,e
road_16 = e,l

# Append to road list
road_list = [road_1, road_2, road_3, road_4, road_5, 
             road_6, road_7, road_8, road_9, road_10, 
             road_11, road_12, road_13, road_14, road_15, road_16]

# Create road network
sim.create_roads(road_list)

# Start simulation
win = Window(sim)
win.zoom = 8
win.run(steps_per_update=5)