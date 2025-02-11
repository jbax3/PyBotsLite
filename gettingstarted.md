

# Welcome to PyBots!

PyBots is a fun and interactive web platform where you can code your very own robot using Python—right in your web browser!

PyBots wants to assume no knowledge about coding, but also wants to offer high-level concepts that teach you things found only in college engineering courses and aren't on your common coding pathway on a platform like LeetCode.

## How Does It Work?

There's a _Python Object_, `racer` that is built from a _library_ that gives you a variety of starting-blocks of code to choose from.

## Available Methods & Concepts

Here are some methods and ideas to get you started:

- `racer.move_forward(distance, speed)`: Moves the robot straight ahead.
- `racer.apply_power(left, right)`: Sets the left and right motor speeds (think of these as the wheels’ power levels).
- `racer.follow_path(distance, speed, set_point, k_p, x, y)`: Uses a simple proportional controller to follow a path based on sensor readings.
- `racer.sensor_val`: A value representing what the sensor sees. You can use this to build your own control algorithms!

## Getting Started

To begin coding:

1. Write your control algorithm in the provided editor on the left.
2. Click the "Run Code" button to send your Python code to the robot.
3. The simulation updates in real time. Watch the robot move and its sensor values change in the console below.

Try modifying the `racer_control()` function to experiment with different control strategies.

## Have Fun!

PyBots is all about learning through play. Explore the methods, tweak your code, and see how your changes affect the robot. There’s no wrong way to experiment—every change is a step toward becoming a better coder and engineer.