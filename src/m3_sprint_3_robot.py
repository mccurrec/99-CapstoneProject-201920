import mqtt_remote_method_calls as com
import time

def forward_press(base_speed,robot):
    robot.drivesystem.go(base_speed,base_speed)

def backward_press(base_speed,robot):
    robot.drivesystem.go(-base_speed,-base_speed)

def left_press(base_speed,robot):
    robot.drivesystem.go(-base_speed,base_speed)

def right_press(base_speed,robot):
    robot.drivesystem.go(base_speed,-base_speed)

def auto_race_lightning(base_speed,robot):
    racing_speed = base_speed + 100
    turn_speed = base_speed
    item_speed = racing_speed
    robot.drivesystem.go(racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drivesystem.go(item_speed-100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color() == 3:
            robot.drivesystem.go(item_speed+100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color() == 4:
            robot.drivesystem.left_motor.turn_on(item_speed)
            robot.drivesystem.right_motor.turn_on(-item_speed)
        if robot.sensor_system.color_sensor.get_color() == 2:
            turns(robot)
            robot.drivesystem.go(racing_speed)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
            time.sleep(.1)
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
                robot.drivesystem.stop()
                avoid_obstacle(turn_speed,robot)
                robot.drivesystem.go(racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 7:
            time.sleep(3)
            robot.drivesystem.stop()
            celebrate_finish(robot)
            break
    print('Congratulations! You Win!')


def auto_race_sally(base_speed,robot):
    racing_speed = base_speed
    turn_speed = base_speed
    item_speed = racing_speed + 50
    robot.drivesystem.go(racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drivesystem.go(item_speed-100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color() == 3:
            robot.drivesystem.go(item_speed+100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color() == 4:
            robot.drivesystem.left_motor.turn_on(item_speed)
            robot.drivesystem.right_motor.turn_on(-item_speed)
        if robot.sensor_system.color_sensor.get_color() == 2:
            turns(robot)
            robot.drivesystem.go(racing_speed)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
            time.sleep(.1)
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
                robot.drivesystem.stop()
                avoid_obstacle(turn_speed,robot)
                robot.drivesystem.go(racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 7:
            time.sleep(3)
            robot.drivesystem.stop()
            celebrate_finish(robot)
            break
    print('Congratulations! You Win!')

def auto_race_doc(base_speed,robot):
    racing_speed = base_speed
    turn_speed = base_speed + 50
    item_speed = racing_speed
    robot.drivesystem.go(racing_speed)
    robot.sensor_system.color_sensor.mode = 'COL-COLOR'
    while True:
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drivesystem.go(item_speed-100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color() == 3:
            robot.drivesystem.go(item_speed+100)
            time.sleep(4)
        if robot.sensor_system.color_sensor.get_color() == 4:
            robot.drivesystem.left_motor.turn_on(item_speed)
            robot.drivesystem.right_motor.turn_on(-item_speed)
        if robot.sensor_system.color_sensor.get_color() == 2:
            turns(robot)
            robot.drivesystem.go(racing_speed)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
            time.sleep(.1)
            if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 6:
                robot.drivesystem.stop()
                avoid_obstacle(turn_speed,robot)
                robot.drivesystem.go(racing_speed)
        if robot.sensor_system.color_sensor.get_color() == 7:
            time.sleep(3)
            robot.drivesystem.stop()
            celebrate_finish(robot)
            break
    print('Congratulations! You Win!')

def turns(robot):
    white = 94
    black = 23
    k = 0.6
    c = 7
    while True:
        current = robot.sensor_system.color_sensor.get_reflected_light_intensity()
        print(c * (white - current) + c, k * (current - black) + c)
        robot.drive_system.go(k * (white - current) + c, k * (current - black) + c)
        print(robot.sensor_system.color_sensor.get_color_as_name())
        if robot.sensor_system.color_sensor.get_color() == 2:
            time.sleep(0.1)
            if robot.sensor_system.color_sensor.get_color() == 2:
                robot.drive_system.stop()
                break

def avoid_obstacle(turn_speed,robot):
    robot.drivesystem.go(turn_speed)
    if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
        robot.drive_system.stop()
        robot.arm_and_claw.raise_arm()
        robot.drivesystem.right_motor.turn_on(turn_speed)
        robot.drivesystem.left_motor.turn_on(-turn_speed)
        time.sleep(.3)
        robot.drivesystem.stop()
        robot.arm_and_claw.lower_arm()
        robot.drivesystem.right_motor.turn_on(-turn_speed)
        robot.drivesystem.left_motor.turn_on(turn_speed)
        time.sleep(.3)

def celebrate_finish(robot):
    robot.sound_system.speech_maker.speak('yay we won').wait()
    robot.sound_system.speech_maker.speak('good job').wait()
    robot.sound_system.speech_maker.speak('now watch me dance').wait()
    for _ in range(7):
        robot.drivesystem.right_motor.turn_on(100)
        robot.drivesystem.left_motor.turn_on(-100)


