import time
import m1_individual
import m1_rosebot
import mqtt_remote_method_calls


def go_to_target(robot):
    print('going to zone')
    follow_path(robot, 5)


def return_to_target(robot):
    print('returning to zone')
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
    print('retrieving package')
    robot.arm_and_claw.lower_arm()
    robot.drive_system.go(50, -50)
    time.sleep(.5)
    m1_individual.m1_spin_ccw(.5, .05, robot)
    robot.drive_system.go(-50, 50)
    time.sleep(3)
    robot.drive_system.go_straight_until_color_is(5, 50)
    robot.drive_system.go_straight_until_color_is_not(5, 50)
    robot.drive_system.stop()


def deliver_package(robot):
    print('delivering package')
    # after retrieving a package and being lined up to begin follow, follows the path back to the delivery zone:
    follow_path(robot, 5)
    # turns the cw for 0.5 sec to ensure it doesn't miss a package:
    robot.drive_system.go(50, -50)
    time.sleep(.5)
    # the robot turns ccw until it sees a cube that's already been placed or the delivery target:
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 10)
    # then goes forward to place the cube and places it:
    robot.drive_system.go_straight_for_inches_using_encoder(8, 50)
    robot.arm_and_claw.lower_arm()
    # then turns around 180:
    robot.drive_system.go(-50, 50)
    time.sleep(3)
    # then goes up to the red, then across the red, and stops:
    robot.drive_system.go_straight_until_color_is(5, 50)
    robot.drive_system.go_straight_until_color_is_not(5, 50)
    robot.drive_system.stop()


def sort_packages(robot, number_of_packages, mqtt):
    # mqtt = mqtt_remote_method_calls.MqttClient()
    print('sorting packages')
    progress = 0
    mqtt.send_message('update_progress', [progress])
    # starting from the delivery zone, the robot goes to the retrieval zone:
    go_to_target(robot)
    for _ in range(number_of_packages):
        # retrieves package:
        retrieve_package(robot)
        robot.drive_system.go(50, -50)
        time.sleep(0.25)
        # delivers package:
        deliver_package(robot)
        progress = progress + 100 / number_of_packages
        mqtt.send_message('update_progress', [progress])
        print('sent the updated progress value of {}'.format(progress))
        robot.drive_system.go_straight_until_color_is_not(5, 50)
        go_to_target(robot)
    # returns to the retrieval zone:
    go_to_target(robot)


def follow_path(robot, stop):
    print('following path')
    white = 94
    black = 23
    c = 10
    k = 0.7
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        # print(c * (white - current) + c, k * (current - black) + c)
        robot.drive_system.go(k * (white - current) + c, k * (current - black) + c)
        # print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color() == stop:
            time.sleep(0.1)
            if robot.sensor_system.color_sensor.get_color() == stop:
                robot.drive_system.stop()
                break


def follow_path_backwards(robot, stop):
    print('following path backwards')
    white = 94
    black = 23
    c = 10
    k = - 0.7
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        # print(-k * (white - current) + c, -k * (current - black) + c)
        robot.drive_system.go(-k * (white - current) + c, -k * (current - black) + c)
        # print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color() == stop:
            time.sleep(0.1)
            if robot.sensor_system.color_sensor.get_color() == stop:
                robot.drive_system.stop()
                break


def back_track_using_encoder(robot, left_degrees, right_degrees):
    print('back tracking using encoder')
    robot.drive_system.go(50, -50)
    time.sleep(2.55)
    robot.drive_system.stop()
    robot.drive_system.left_motor.reset_position()
    robot.drive_system.right_motor.reset_position()
    robot.drive_system.go(50, 50)
    while True:
        if robot.drive_system.left_motor.get_position() >= right_degrees - 650:
            robot.drive_system.left_motor.turn_off()
        if robot.drive_system.right_motor.get_position() >= left_degrees - 650:
            robot.drive_system.right_motor.turn_off()
        if robot.drive_system.left_motor.get_position() >= right_degrees - 650 and \
                robot.drive_system.right_motor.get_position() >= left_degrees - 650:
            break
    robot.drive_system.stop()


def return_value(robot):
    print(robot.sensor_system.color_sensor.get_color_as_name())


def old_retrieve_package(robot):
    print('retrieving package')
    robot.arm_and_claw.lower_arm()
    robot.drive_system.left_motor.reset_position()
    robot.drive_system.right_motor.reset_position()
    robot.drive_system.go(50, -50)
    time.sleep(.5)
    m1_individual.m1_spin_ccw(.5, .05, robot)
    left_degrees = robot.drive_system.left_motor.get_position()
    right_degrees = robot.drive_system.right_motor.get_position()
    back_track_using_encoder(robot, left_degrees, right_degrees)


def old_deliver_package(robot):
    print('delivering package')
    # follows the path back to the delivery zone:
    follow_path(robot, 5)
    # resets the encoders:
    robot.drive_system.left_motor.reset_position()
    robot.drive_system.right_motor.reset_position()
    # turns the cw for 0.5 sec to ensure it doesn't miss a package:
    robot.drive_system.go(50, -50)
    time.sleep(.5)
    # the robot turns ccw until it sees a cube that's already been placed or the delivery target:
    robot.drive_system.spin_counterclockwise_until_sees_object(50, 10)
    # then it turns cw slightly to align better then stops:
    robot.drive_system.go(50, -50)
    time.sleep(.02)
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(2, 50)
    robot.arm_and_claw.lower_arm()
    # the robot turns back around and goes back to the track:
    left_degrees = robot.drive_system.left_motor.get_position()
    right_degrees = robot.drive_system.right_motor.get_position()
    back_track_using_encoder(robot, left_degrees, right_degrees)


