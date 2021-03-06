import time


def m3_feature_9(initial_rate, rate_of_increase,robot):
    # starts the robot at the given speed:
    robot.drive_system.go(50, 50)
    robot.drive_system.left_motor.reset_position()
    # stores the distance to the cube as previous distance:
    previous_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    # stores the current time as the previous time:
    previous_time = time.time()
    # set the rate between beeps as the initial rate given by the user:
    rate = initial_rate
    # delta is the distance needed to travel for the beeping to increase in speed by the given increment:
    delta = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / ((robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - 0.01) / rate_of_increase)
    # loops until the cube is reached and picked up:
    while True:
        # checks to see if the change in distance to the cube is greater than delta:
        if robot.drive_system.left_motor.get_position() - previous_distance >= delta:
            # checks to see if enough time has passed from the last beep:
            if time.time() - previous_time >= rate:
                previous_distance = robot.drive_system.left_motor.get_position()
                previous_time, rate = m3_feature_9_cycle_and_time_faster(rate, rate_of_increase,robot)
                # previous_time, rate = m1_individual.m1_feature_9_beep_and_time_faster(rate,rate_of_increase,self.robot)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break


def m3_feature_9_cycle_and_time_faster(rate, rate_of_increase,robot):
    robot.led_system.left_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()  # the time from last beep is reset:
    return time.time(), rate - rate_of_increase

def m3_feature_10(speed, direction,robot):
    if direction == "clockwise":
        robot.drive_system.spin_clockwise_until_sees_object(speed,10)
        robot.drive_system.left_motor.turn_on(-50)
        robot.drive_system.right_motor.turn_on(50)
        time.sleep(.07)
    elif direction == "counterclockwise":
        robot.drive_system.spin_counterclockwise_until_sees_object(speed, 10)
        robot.drive_system.left_motor.turn_on(50)
        robot.drive_system.right_motor.turn_on(-50)
        time.sleep(.02)
    m3_feature_9(.05,.005,robot)