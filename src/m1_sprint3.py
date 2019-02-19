import time
import m1_individual
import rosebot


def go_to_target(robot):
    follow_path(robot, 5)


def return_to_target(robot):
    robot.drive_system.go(-50, 50)
    time.sleep(2)
    while True:
        if robot.sensor_system.color_sensor.get_reflected_light_intensity() <= 30:
            break
    robot.drive_system.go(50, 50)
    time.sleep(.25)
    follow_path_backwards(robot, 5)
    # robot.drive_system.go(-50, 50)
    # time.sleep(.55)
    robot.drive_system.go(50, 50)
    time.sleep(0.25)
    follow_path(robot, 5)


def retrieve_package(robot):
    robot.drive_system.go(50, -50)
    time.sleep(.5)
    m1_individual.m1_spin_cw(.5, .05, robot)


def deliver_package(robot):
    pass


def sort_packages(robot, number_of_packages):
    pass


def follow_path(robot, stop):
    white = 94
    black = 23
    k = 0.6
    c = 7
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        print(c * (white - current) + c, k * (current - black) + c)
        robot.drive_system.go(k * (white - current) + c, k * (current - black) + c)
        print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color() == stop:
            time.sleep(0.1)
            if robot.sensor_system.color_sensor.get_color() == stop:
                robot.drive_system.stop()
                break


def follow_path_backwards(robot, stop):
    white = 94
    black = 23
    k = -0.6
    c = -7
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        print(k * (white - current) + c, k * (current - black) + c)
        robot.drive_system.go(k * (white - current) + c, k * (current - black) + c)
        print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color() == stop:
            time.sleep(0.1)
            if robot.sensor_system.color_sensor.get_color() == stop:
                robot.drive_system.stop()
                break


def return_value(robot):
    print(robot.sensor_system.color_sensor.get_reflected_light_intensity())


