# Intelligent Mobile Robot Navigation Using Computational Intelligence Techniques

## Project Description
This project was developed for the Computational Intelligence Mini Project. The objective is to design and simulate an intelligent mobile robot that can navigate from a start point to a goal point while avoiding obstacles in the environment.

Two navigation approaches were implemented:
- Rule-Based Navigation
- Fuzzy Logic Navigation

The performance of both approaches was compared using several evaluation metrics.

## Software and Tools
- Python 3.11
- Visual Studio Code
- NumPy
- Matplotlib
- Scikit-Fuzzy

## Project Files

### map1.py
Creates a simple robot navigation environment.

### map2.py
Creates a more complex navigation environment with additional obstacles.

### intelligent_robot.py
Implements a rule-based robot navigation controller.

### fuzzy_navigation.py
Implements a fuzzy logic navigation controller for obstacle avoidance.

### evaluation.py
Compares the performance of Rule-Based and Fuzzy Logic navigation methods.

## Evaluation Results

| Metric | Rule-Based Robot | Fuzzy Logic Robot |
|----------|----------|----------|
| Success Rate | 85% | 95% |
| Path Length | 12.8 | 11.2 |
| Collisions | 1 | 0 |
| Time Steps | 20 | 18 |

## Conclusion
Both navigation methods successfully guided the robot to the goal position. However, the Fuzzy Logic controller achieved better performance with a higher success rate, shorter path length, fewer collisions, and fewer time steps. This demonstrates the effectiveness of Computational Intelligence techniques in robot navigation.

## Author
Muhammad Hamim Zafran Bin Zaharuddin

Matric Number: 2519605

## Course
MCTA3371 Computational Intelligence

## Lecturer
Dr. Azhar Bin Mohd Ibrahim
