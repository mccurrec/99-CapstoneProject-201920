import time
import math
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import rosebot


def m2_feature_9(freq, iteration, robot):
    robot.drive_system.go(50, 50)
    robot.drive_system.left_motor.reset_position()
    start = robot.drive_system.left_motor.get_position()

    while True:
        if robot.drive_system.left_motor.get_position() - start >= 90:
            robot.sound_system.tone_maker.play_tone(freq, 500)
            freq = int(freq) + int(iteration)
            start = robot.drive_system.left_motor.get_position()

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
            # if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 0.25:
            # if self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 0.25:

            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()

            break


def m2_feature_10(freq, iteration, direction, robot):
    if direction == "clockwise":
        robot.drive_system.spin_clockwise_until_sees_object(50, 10)
        robot.drive_system.left_motor.turn_on(-50)
        robot.drive_system.right_motor.turn_on(50)
        time.sleep(.07)
    elif direction == "counterclockwise":
        robot.drive_system.spin_counterclockwise_until_sees_object(50, 10)
        robot.drive_system.left_motor.turn_on(50)
        robot.drive_system.right_motor.turn_on(-50)
        time.sleep(.02)
    m2_feature_9(freq, iteration, robot)

def plow(between, length, how_many, robot):



    for k in range(how_many):
        robot




