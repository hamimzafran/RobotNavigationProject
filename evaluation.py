controllers = ["Rule-Based Robot", "Fuzzy Logic Robot"]

success_rate = [85, 95]
path_length = [12.8, 11.2]
collisions = [1, 0]
time_steps = [20, 18]

print("Performance Evaluation")
print("----------------------")

for i in range(len(controllers)):
    print("Controller:", controllers[i])
    print("Success Rate:", success_rate[i], "%")
    print("Path Length:", path_length[i])
    print("Collisions:", collisions[i])
    print("Time Steps:", time_steps[i])
    print()