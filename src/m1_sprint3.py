import time
import rosebot


def return_to_start(robot):
    follow_path(robot, 'Blue')


def go_to_end(robot):
    follow_path(robot, 'Red')


def retrieve_package(robot):
    pass


def deliver_package(robot):
    pass


def sort_packages(robot, number_of_packages):
    pass


def line_follow_in_loop(robot):
    error = 7  # adjust to make the run smoother
    speed = 50  # add an entry for this
    original = robot.sensor_system.color_sensor.get_reflected_light_intensity()
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        if original - error < current < original + error:
            robot.drive_system.go(speed, speed)
        else:
            robot.drive_system.left_motor.turn_on(50)
            robot.drive_system.right_motor.turn_on(-50)


def line_follow_in_loop_PID(robot, stop):
    B = 35
    k1 = -0.45
    k2 = 0.45
    original = robot.sensor_system.color_sensor.get_reflected_light_intensity()
    print('Original =', original)
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        error = current - original
        robot.drive_system.go(B + error * k1, B + error * k2)
        if robot.sensor_system.color_sensor.get_color_as_name() == stop:
            robot.drive_system.stop()


def follow_path(robot, stop):
    white = 94
    black = 23
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        print(0.5 * (white - current) + 15, 0.5 * (current - black) + 15)
        robot.drive_system.go(0.5 * (white - current) + 15, 1 * (current - black) + 15)
        print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color_as_name() == stop:
            robot.drive_system.stop()


def return_value(robot):
    print(robot.sensor_system.color_sensor.get_reflected_light_intensity())


