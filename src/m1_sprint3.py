import time
import rosebot


def go_to_target(robot):
    follow_path(robot, 2)


def return_to_target(robot):
    robot.drive_system.go(-50, 50)
    time.sleep(3)
    robot.drive_system.go_straight_until_color_is(2, -50)
    follow_path(robot, 2)


def retrieve_package(robot):
    pass


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


