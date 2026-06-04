import matplotlib.pyplot as plt

start = (1, 1)
goal = (9, 9)

obstacles_x = [3,4,5,6,7,3,7]
obstacles_y = [3,3,3,3,3,6,6]

plt.figure(figsize=(6,6))

plt.scatter(start[0], start[1], s=200)
plt.text(start[0], start[1], "START")

plt.scatter(goal[0], goal[1], s=300)
plt.text(goal[0], goal[1], "GOAL")

plt.scatter(obstacles_x, obstacles_y, s=300)

plt.xlim(0,10)
plt.ylim(0,10)

plt.grid()

plt.show()