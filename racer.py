# racer.py
from math import sin, cos, atan
import random
from types import MethodType

class Racer:
    def __init__(
        self,
        x_start = 600,        # starting x (canvas coordinates)
        y_start = 525,        # starting y
        racer_width = 50,
        racer_height = 75,
        sensor_width = 20,
        sensor_height = 10,
        frame_rate = 1/60,
        angle = 0,
        border_thickness = 10,
        add_noise = False,
        show_trace = False,
        trace_loc = 'center'
    ):
        # Racer state
        self.x = x_start
        self.y = y_start
        self.racer_width = racer_width
        self.racer_height = racer_height
        self.angle = angle  # in radians
        # Sensor parameters
        self.sensor_width = sensor_width
        self.sensor_height = sensor_height
        self.hy = (sensor_width**2 + sensor_height**2) ** 0.5  # used for PIP sizing
        self.add_noise = add_noise
        self.sensor_val = 120  # default; will be updated by JavaScript
        # Motor speeds (pixels/second)
        self.left_motor_speed = 0
        self.right_motor_speed = 0
        self.left_motor_speed_m1 = 0
        self.right_motor_speed_m1 = 0
        self.power_consumed = 0
        # Timing
        self.frame_rate = frame_rate

    def run_physics(self):
        """Advance the car’s state using a simple differential‐drive model."""
        self.angle += atan((self.left_motor_speed - self.right_motor_speed) / self.racer_width)
        self.x += sin(self.angle) * (self.left_motor_speed + self.right_motor_speed) / 2
        self.y -= cos(self.angle) * (self.left_motor_speed + self.right_motor_speed) / 2

    def calc_power_consumed(self):
        """Accumulate power consumption from changes in motor speeds."""
        self.power_consumed += (abs(self.left_motor_speed - self.left_motor_speed_m1) +
                                abs(self.right_motor_speed - self.right_motor_speed_m1))
        self.left_motor_speed_m1 = self.left_motor_speed
        self.right_motor_speed_m1 = self.right_motor_speed

    def calc_environment_variables(self):
        """Update any derived environment variables (here, just power consumed)."""
        self.calc_power_consumed()

    def update(self, dt):
        """Advance simulation by dt seconds (physics and environment variables)."""
        self.run_physics()
        self.calc_environment_variables()

    def move_forward(self, distance=10, speed=1):
        """Move straight ahead for a given distance at a given speed."""
        self.left_motor_speed = speed
        self.right_motor_speed = speed
        n = int(abs(distance / speed))
        def run_physics(self):
            self.angle += atan((self.left_motor_speed - self.right_motor_speed) / self.racer_width)
            self.x += sin(self.angle) * (self.left_motor_speed + self.right_motor_speed) / 2
            self.y -= cos(self.angle) * (self.left_motor_speed + self.right_motor_speed) / 2
        self.run_physics = MethodType(run_physics, self)
        for i in range(n):
            self.update(1/60)

    def apply_power(self, left_motor_speed, right_motor_speed):
        """Set the left and right motor speeds."""
        self.left_motor_speed = left_motor_speed
        self.right_motor_speed = right_motor_speed

    def follow_path(self, distance=3000, speed=3, set_point=150, k_p=1/25, x=650, y=525):
        """
        Follow a path using a simple proportional controller.
        Motor speeds are adjusted based on the difference between a set point
        and the current sensor value.
        """
        self.x = x
        self.y = y
        def run_physics(self):
            self.left_motor_speed = speed + k_p * (set_point - self.sensor_val)
            self.right_motor_speed = speed - k_p * (set_point - self.sensor_val)
            self.angle += atan((self.left_motor_speed - self.right_motor_speed) / self.racer_width)
            self.x += sin(self.angle) * (self.left_motor_speed + self.right_motor_speed) / 2
            self.y -= cos(self.angle) * (self.left_motor_speed + self.right_motor_speed) / 2
        self.run_physics = MethodType(run_physics, self)
        n = int(abs(distance / speed))
        for i in range(n):
            self.update(1/60)

# Create a global racer instance.
racer = Racer()
