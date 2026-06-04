import matplotlib.pyplot as plt

# Start and goal position
start = (1, 1)
goal = (9, 9)

# Obstacles
obstacles_x = [4, 5, 6]
obstacles_y = [5, 5, 5]

plt.figure(figsize=(6, 6))

# Draw start point
plt.scatter(start[0], start[1], s=200, label="Start")
plt.text(start[0], start[1], "START")

# Draw goal point
plt.scatter(goal[0], goal[1], s=300, label="Goal")
plt.text(goal[0], goal[1], "GOAL")

# Draw obstacles
plt.scatter(obstacles_x, obstacles_y, s=300, label="Obstacles")

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.grid()
plt.legend()
plt.title("Map 1: Simple Navigation Environment")

plt.show()