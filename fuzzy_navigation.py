import matplotlib.pyplot as plt
import math

def fuzzy_steering(obstacle_distance):
    # Simple fuzzy logic rules
    if obstacle_distance < 1.5:
        return 1.0      # strong turn up
    elif obstacle_distance < 2.5:
        return 0.5      # slight turn up
    else:
        return 0.0      # go straight

robot_x = 1
robot_y = 1

goal_x = 9
goal_y = 9

obstacles = [(4, 5), (5, 5), (6, 5)]

path_x = [robot_x]
path_y = [robot_y]

collisions = 0

for step in range(40):
    dx = goal_x - robot_x
    dy = goal_y - robot_y

    distance_to_goal = math.sqrt(dx**2 + dy**2)

    if distance_to_goal < 0.5:
        break

    nearest_obstacle = min(
        math.sqrt((robot_x - ox)**2 + (robot_y - oy)**2)
        for ox, oy in obstacles
    )

    steer = fuzzy_steering(nearest_obstacle)

    move_x = 0.45 * dx / distance_to_goal
    move_y = 0.45 * dy / distance_to_goal

    move_y += steer * 0.5

    next_x = robot_x + move_x
    next_y = robot_y + move_y

    for ox, oy in obstacles:
        if math.sqrt((next_x - ox)**2 + (next_y - oy)**2) < 0.6:
            collisions += 1
            next_y += 1.0

    robot_x = next_x
    robot_y = next_y

    path_x.append(robot_x)
    path_y.append(robot_y)

path_length = 0
for i in range(1, len(path_x)):
    path_length += math.sqrt((path_x[i]-path_x[i-1])**2 + (path_y[i]-path_y[i-1])**2)

plt.figure(figsize=(6,6))

plt.scatter(1, 1, s=200, label="Start")
plt.scatter(9, 9, s=300, label="Goal")

for ox, oy in obstacles:
    plt.scatter(ox, oy, s=300)

plt.plot(path_x, path_y, linewidth=2, label="Fuzzy Logic Path")

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.grid()
plt.legend()
plt.title("Fuzzy Logic Mobile Robot Navigation")
plt.show()

print("Fuzzy Navigation Results")
print("------------------------")
print("Steps:", len(path_x))
print("Path Length:", round(path_length, 2))
print("Collisions:", collisions)
print("Final Distance to Goal:", round(distance_to_goal, 2))