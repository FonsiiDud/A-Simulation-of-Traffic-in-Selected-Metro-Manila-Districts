from trafficSimulator import *

# Create simulation
sim = Simulation()

# params
lane_space = 2
road_length = 50

# Left Main Road Segment Points
left_main_road_start_0 = (-4, 10)
left_main_road_end_0 = (0, 0)
left_main_road_start_1 = (-0, -0)
left_main_road_end_1 = (10, -road_length/2)
left_main_road_start_2 = (10, -road_length/2)
left_main_road_end_2 = (13, -road_length * 2.5)

# Main Horizontal Road Segment Points
main_road_start_0 = left_main_road_end_1
main_road_end_0 = (100, left_main_road_end_1[1])

# Right Main Road Segment Points
right_main_road_start_0 = (100, 0)
right_main_road_end_0 = (100, -100)
right_main_road_start_1 = (84, 40)
right_main_road_end_1 = right_main_road_start_0

# Top Main Road Segment Points
top_main_road_start_0 = right_main_road_end_0 
top_main_road_end_0 = (13, -road_length * 2.5)

# Bottom Main Road Segment Points
bottom_main_road_start_0 = left_main_road_start_0
bottom_main_road_end_0 = right_main_road_start_1

############## ROADS ################

# Left Main Road
left_main_road_0 = left_main_road_start_0, left_main_road_end_0
left_main_road_1 = left_main_road_start_1, left_main_road_end_1
left_main_road_2 = left_main_road_start_2, left_main_road_end_2

left_main_road_roads = [left_main_road_0, left_main_road_1, left_main_road_2]

# Main Horizontal Road
main_road_0 = main_road_start_0, main_road_end_0

main_road_roads = [main_road_0]

# Right Main Road
right_main_road_0 = right_main_road_start_0, right_main_road_end_0
right_main_road_1 = right_main_road_start_1, right_main_road_end_1

right_main_road_roads = [right_main_road_0 , right_main_road_1]

# Top Main Road
top_main_road_0 = top_main_road_start_0, top_main_road_end_0

top_main_road_roads = [top_main_road_0]

# Bottom Main Road
bottom_main_road_0 = bottom_main_road_start_0, bottom_main_road_end_0

bottom_main_road_roads = [bottom_main_road_0]






road_coord_collection = [left_main_road_roads, main_road_roads, right_main_road_roads, top_main_road_roads, bottom_main_road_roads]

road_array = []

for road_collection in road_coord_collection:
    for road in road_collection:
        road_array.append(road)

sim.create_roads(road_array)



# Start simulation
win = Window(sim)
win.zoom = 8
win.run(steps_per_update=5)