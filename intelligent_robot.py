import matplotlib.pyplot as plt
import math

# Start and Goal
robot_x = 1
robot_y = 1

goal_x = 9
goal_y = 9

# Obstacles
obstacles = [(4,5),(5,5),(6,5)]

path_x = [robot_x]
path_y = [robot_y]

for step in range(20):

    dx = goal_x - robot_x
    dy = goal_y - robot_y

    # move toward goal
    next_x = robot_x + 0.5 * dx/math.sqrt(dx*dx + dy*dy)
    next_y = robot_y + 0.5 * dy/math.sqrt(dx*dx + dy*dy)

    # simple obstacle avoidance
    for ox, oy in obstacles:
        distance = math.sqrt((next_x-ox)**2 + (next_y-oy)**2)

        if distance < 2.0 :
            next_y += 1

    robot_x = next_x
    robot_y = next_y

    path_x.append(robot_x)
    path_y.append(robot_y)

plt.figure(figsize=(6,6))

plt.scatter(1,1,s=200,label="Start")
plt.scatter(9,9,s=300,label="Goal")

for ox,oy in obstacles:
    plt.scatter(ox,oy,s=300)

plt.plot(path_x,path_y,'b-',linewidth=2)

plt.xlim(0,10)
plt.ylim(0,10)

plt.grid()
plt.legend()

plt.show()